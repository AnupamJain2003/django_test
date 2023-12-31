from django.contrib.auth.base_user import BaseUserManager

class userManager(BaseUserManager):

    def create_user(self,username,email,password=None,**extra_feids):
        
        email=self.normalize_email(email)
        user=self.model(username=username ,email=email,**extra_feids)
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self,email,password=None,**extra_feids):
        extra_feids.setdefault('is_staff',True)
        extra_feids.setdefault('is_superuser',True)
        extra_feids.setdefault('is_active',True) 
        
        return self.create_user(email,password,**extra_feids)       
