from datetime import date

from django.contrib.auth import get_user_model
from rest_framework import serializers

from sale_objects.models import Address, Contact, Product, SaleObject

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

    def validate_name(self, name):
        if len(name) > 25:
            raise serializers.ValidationError(
                'Длина названия не должна превышать 25 символов!'
            )
        return name

    def validate_on_sale_date(self, on_sale_date):
        if on_sale_date > date.today():
            raise serializers.ValidationError(
                'Вы указали дату из будущего!'
            )
        return on_sale_date


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ('country', 'city', 'street', 'house',)


class ContactSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Contact
        fields = ('email', 'address')


class SaleObjectReadSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения объктов торговой сети."""
    contacts = ContactSerializer(read_only=True)
    products = ProductSerializer(many=True, read_only=True)
    workers = UserSerializer(many=True, read_only=True)
    parent = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = SaleObject
        fields = (
            'role',
            'name',
            'contacts',
            'products',
            'workers',
            'parent',
            'debt',
            'create_date'
        )


class SaleObjectEditSerializer(serializers.ModelSerializer):
    """Сериализатор для редактирования объктов торговой сети."""
    workers = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        many=True
    )
    products = ProductSerializer(many=True)
    contacts = ContactSerializer()

    class Meta:
        model = SaleObject
        fields = (
            'role',
            'name',
            'contacts',
            'products',
            'workers',
            'parent',
            'debt',
            'create_date'
        )

    def validate_name(self, name):
        if len(name) > 50:
            raise serializers.ValidationError(
                'Длина названия не должна превышать 50 символов!'
            )
        return name

    def create(self, validated_data):
        workers = validated_data.pop('workers')
        products = validated_data.pop('products')
        contacts = validated_data.pop('contacts')
        sale_object = SaleObject.objects.create(**validated_data)
        sale_object.workers.set(workers)
        for product in products:
            current_product, status = Product.objects.get_or_create(**product)
            sale_object.products.add(current_product)
        address = contacts.pop('address')
        cur_address = Address.objects.create(**address)
        cur_contacts = Contact.objects.create(
            email=contacts.get('email'),
            address=cur_address
        )
        sale_object.contacts = cur_contacts
        sale_object.save()
        return sale_object

    def update(self, instance, validated_data):
        if 'debt' in validated_data:
            raise serializers.ValidationError(
                'Обновить задолженность через API не возможно!'
            )
        if 'workers' in validated_data:
            workers = validated_data.pop('workers')
            for worker in workers:
                instance.workers.add(worker)
        if 'products' in validated_data:
            products = validated_data.pop('products')
            for product in products:
                current_product, status = Product.objects.get_or_create(
                    **product
                )
                instance.products.add(current_product)
        if 'contacts' in validated_data:
            contacts = validated_data.pop('contacts')
            if 'address' in contacts:
                address = contacts.pop('address')
                cur_address, status = Address.objects.get_or_create(**address)
                if 'email' in contacts:
                    cur_email = contacts.get('email')
                    cur_contacts, status = Contact.objects.get_or_create(
                        email=cur_email,
                        address=cur_address
                    )
                    instance.contacts = cur_contacts
                    instance.save()
                else:
                    instance.contacts.address = cur_address
                    instance.contacts.save()
            else:
                instance.contacts.email = contacts.get('email')
                instance.contacts.save()
        return super().update(instance, validated_data)
