from django.core.exceptions import ValidationError
import os
import datetime
def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    print(ext)
    valid_extensions = ['.jpg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Debe ser .png o .jpg')

def validate_past_date(value):
    date = datetime.date.today()
    if value.year < date.year :
        raise ValidationError(u'%s is not a valid year!' % value)
