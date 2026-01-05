# from django.contrib import admin

# from platform_web.models.store.subcategory import Subcategory
# from platform_web.models.store.product import Product
# from platform_web.models.store.category import Category
# from platform_web.models.store.product_image import ProductImage
# from platform_web.models.store.review import Review
# from platform_web.models.store.attribute import Attribute, AttributeValue


# # inlines
# class InlineProductImage(admin.TabularInline):
#     model = ProductImage
#     extra = 1


# # inlines -> linked to main
# class ProductInlines(admin.ModelAdmin):
#     inlines = [InlineProductImage]


# admin.site.register(Product, ProductInlines)
# admin.site.register(Category)
# admin.site.register(Review)
# admin.site.register(Attribute)
# admin.site.register(AttributeValue)
# admin.site.register(Subcategory)
