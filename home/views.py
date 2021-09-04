# https://stackoverflow.com/questions/6481279/django-sum-query
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Bayar, SaldoAwal, Pengeluaran, Pinjaman
import datetime
from django.db.models import Sum
from django.shortcuts import get_object_or_404

from accounts.decorators import unauthenticated_user, allowed_users
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required




@method_decorator([login_required, allowed_users(allowed_roles=['admin'])], name='dispatch') 
class HomeView(ListView):
    template_name ='dashboard.html'
    model =  SaldoAwal
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        nows = datetime.datetime.now()
        monyer = nows.strftime("%B-%Y")
        day = nows.strftime("%d")
        mont = nows.strftime("%m")
        saldos = SaldoAwal.objects.get(month=f"{monyer}",nama_id="1")
        pengeluaran_day = Pengeluaran.objects.all()
        
        pinjaman = Pinjaman.objects.all()
        bayar = Bayar.objects.all()

        query_day = pengeluaran_day.filter(tanggal__day=f"{day}", nama_id="1").aggregate(Sum("nominal"))
        query_month =  pengeluaran_day.filter(tanggal__month=f"{mont}", nama_id="1").aggregate(Sum("nominal"))
        
        if query_month['nominal__sum'] == None:
            pinjam_month =  pinjaman.filter(tanggal__month=f"{mont}").aggregate(Sum("nominal"))
            bayar_month =  bayar.filter(tanggal__month=f"{mont}").aggregate(Sum("nominal"))
            sisa = saldos.nominal - 0
            sisa_pinjam = 0 - 0
        else:
        
            pinjam_month =  pinjaman.filter(tanggal__month=f"{mont}").aggregate(Sum("nominal"))
            bayar_month =  bayar.filter(tanggal__month=f"{mont}").aggregate(Sum("nominal"))
            # print(query_month['nominal__sum'])
            sisa = saldos.nominal - query_month['nominal__sum']
        
            print(bayar_month['nominal__sum'])
            sisa_pinjam = pinjam_month['nominal__sum'] - bayar_month['nominal__sum']
        context['saldo'] = saldos
        context['pengeluaran_day'] = query_day
        context['pengeluaran_month'] = query_month
        context['sisa'] = sisa
        context['tot_pinjam'] = pinjam_month
        context['sisa_pinjam'] = sisa_pinjam
        
        context['pengeluaral_all'] = pengeluaran_day
        context['pinjaman_all'] = pinjaman

        print(pinjam_month)
        return context
    

# class HomeView(TemplateView):
#     template_name ='dashboard.html'
#     model   = SaldoAwal
    
#     def get_context_data(self, **kwargs):

#         context = super(HomeView, self).get_context_data(**kwargs)
#         nows = datetime.datetime.now()
#         monyer = nows.strftime("%B-%Y")
#         day = nows.strftime("%d")
#         mont = nows.strftime("%m")
#         saldos = SaldoAwal.objects.get(month=f"{monyer}",nama_id="1")
#         pengeluaran_day = Pengeluaran.objects.get(tanggal__day="08", nama_id="1")
       
#         # pengeluaran_day = Pengeluaran.objects.get(tanggal__day=f"{day}", nama_id="1")
#         # pengeluaran_mon = Pengeluaran.objects.get(tanggal__month="08", nama_id="1")
#         # print(pengeluaran_mon)
        
#         context = {
#             'saldo': saldos,
#             'pengeluaran_day': pengeluaran_day
#         }
#         # context.update(kwargs)
        
#         # context['saldo'] = saldos
#         # context['pengeluaran_day'] = pengeluaran_day.get(tanggal__day="08", nama_id="1")
#         # context['pengeluaran_month'] = pengeluaran_day.filter(tanggal__month="08", nama_id="1").aggregate(Sum("nominal"))
#         return context
    
