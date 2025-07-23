# services/models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    requires_documents = models.TextField(blank=True, help_text="قائمة الوثائق المطلوبة مفصولة بفواصل")

    def __str__(self):
        return self.name

    @staticmethod
    def load_defaults():
        defaults = [
            ("استخراج بطاقة هوية وطنية جديدة", "طلب إصدار هوية لأول مرة", "صورة شخصية، بيان ولادة"),
            ("تجديد بطاقة الهوية الوطنية", "تجديد الهوية المنتهية", "صورة الهوية القديمة"),
            ("استخراج بدل ضائع لبطاقة الهوية", "إصدار هوية بدل ضائع", "بلاغ فقدان من الشرطة"),
            ("إخراج قيد فردي", "وثيقة إخراج قيد فردي من السجل المدني", "بيان ولادة"),
            ("إخراج قيد عائلي", "وثيقة عائلية تشمل أفراد الأسرة", "دفتر العائلة"),
            ("تعديل الحالة الاجتماعية", "تحديث الحالة الاجتماعية في السجلات", "صك الزواج أو الطلاق"),
            ("تسجيل مولود جديد", "إضافة مولود إلى السجل المدني", "شهادة ولادة، هوية الأب والأم"),
            ("طلب جواز سفر جديد", "إصدار جواز سفر لأول مرة", "صورة شخصية، الهوية"),
            ("تجديد جواز سفر", "تجديد جواز سفر منتهي", "الجواز القديم"),
            ("استخراج بدل ضائع لجواز السفر", "بدل فاقد لجواز السفر", "بلاغ شرطة"),
            ("تجديد شهادة قيادة", "تجديد رخصة القيادة المنتهية", "الرخصة القديمة"),
            ("بدل ضائع لشهادة القيادة", "إصدار بدل فاقد لرخصة القيادة", "بلاغ من الشرطة"),
            ("تسجيل مركبة جديدة", "طلب تسجيل مركبة لأول مرة", "فواتير شراء المركبة، شهادة جمرك"),
            ("فحص فني للمركبة", "حجز موعد للفحص الفني", "بطاقة المركبة"),
            ("بيان عقاري", "وثيقة تملك عقاري", "سند التمليك"),
            ("نقل ملكية عقار", "طلب نقل ملكية بين الأطراف", "عقد البيع، سند التمليك"),
            ("وثيقة تخرج جامعية", "طلب شهادة تخرج", "الرقم الجامعي"),
            ("تصديق شهادة مدرسية أو جامعية", "توثيق الشهادة الدراسية", "نسخة أصلية من الشهادة"),
            ("براءة ذمة تأمينات", "إثبات عدم وجود مستحقات تأمينات", "رقم التأمين"),
            ("سجل عدلي", "طلب وثيقة غير محكوم", "الهوية الشخصية")
        ]
        for name, desc, docs in defaults:
            Service.objects.get_or_create(name=name, defaults={"description": desc, "requires_documents": docs})


class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=150)
    national_id = models.CharField(max_length=15)
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='قيد المعالجة', choices=[
        ('قيد المعالجة', 'قيد المعالجة'),
        ('مرفوض', 'مرفوض'),
        ('مقبول', 'مقبول')
    ])

    def __str__(self):
        return f"{self.service.name} - {self.user.username}"
