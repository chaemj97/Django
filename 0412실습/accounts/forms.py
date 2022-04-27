from dataclasses import field
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        # 수정 필요한 필드만 작성
        fields = ('email','first_name','last_name')