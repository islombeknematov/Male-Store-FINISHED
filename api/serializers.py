# Serializers allow complex data such as querysets and model
# instances to be converted to native Python datatypes that can
# then be easily rendered into JSON, XML or other content types.
# Serializers also provide deserialization, allowing parsed data to be
# converted back into complex types, after first validating the incoming data.

# Serializer is data, in which format is going out from model
# and in which format is coming from user

from rest_framework import serializers

from products.models import CategoryModel, ProductModel, BrandModel, SizeModel, ProductTagModel, ColorModel


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        exclude = ['title_ru', 'title_uz', 'title_en']


class BrandModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandModel
        fields = '__all__'


class SizeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeModel
        fields = '__all__'


class TagModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTagModel
        fields = '__all__'


class ColorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorModel
        fields = '__all__'


class ProductModelSerializer(serializers.ModelSerializer):
    category = CategoryModelSerializer()
    brand = BrandModelSerializer()
    colors = ColorModelSerializer(many=True)
    tags = TagModelSerializer(many=True)
    sizes = SizeModelSerializer(many=True)

    class Meta:
        model = ProductModel
        exclude = ['title_ru', 'title_uz', 'title_en',
                   'short_description_ru', 'short_description_uz', 'short_description_en',
                   'long_description_ru', 'long_description_uz', 'long_description_en']
