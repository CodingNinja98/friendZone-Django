from django.contrib import admin
from project.models import register,Post,activity,education,followUsers,notify,inbox,likes,postcomment,interest,contact


# Register your models here.
admin.site.register(register)
admin.site.register(Post)
admin.site.register(activity)
admin.site.register(education)
admin.site.register(followUsers)
admin.site.register(notify)
admin.site.register(inbox)
admin.site.register(likes)
admin.site.register(postcomment)
admin.site.register(interest)
admin.site.register(contact)
