from django import forms

G=[('male','male'),('female','female')]
course=[('python','python'),('sql','sql'),('webtechnology','webtechnology'),('django','django')]

class form(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField(min_value=10)
    email=forms.EmailField()
    passwords=forms.CharField(max_length=100,widget=forms.PasswordInput)
    address=forms.CharField(max_length=1000,widget=forms.Textarea(attrs={'cols':10,'rows':10}))
    #gender=forms.ChoiceField(choices=G)
    gender=forms.ChoiceField(choices=G,widget=forms.RadioSelect)
    #course=forms.ChoiceField(choices=course)
    course=forms.MultipleChoiceField(choices=course,widget=forms.CheckboxSelectMultiple)