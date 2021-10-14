from django.contrib import admin

# Register your models here.
from .models import customer,Product,Order,Category,Status,Photo



admin.site.register(customer )
admin.site.register(Category )
admin.site.register(Status )
admin.site.register(Order )
admin.site.register(Photo)
admin.site.register(Product )

admin.site.index_title = 'BadAss GFx'
admin.site.site_header = 'GFX_Badass'
admin.site.site_title = 'Welcome TO GFX'


