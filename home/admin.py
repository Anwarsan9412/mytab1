from django.contrib import admin

from .models import Profile, Pinjaman, SaldoAwal, StatusPinjam, Pengeluaran, Bayar

admin.site.register(Profile)
admin.site.register(Pinjaman)
admin.site.register(Bayar)
admin.site.register(StatusPinjam)
admin.site.register(Pengeluaran)

@admin.register(SaldoAwal)
class SaldoAwalAdmin(admin.ModelAdmin):
    fields = ('nama', 'nominal')
    list_display = ('nama','nominal','month')
    # list_filter = ('event_date','venue')
    ordering = ('-date_created',)
