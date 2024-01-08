# app_21035/views.py
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import ProductFamily, Product, SellingPoint, Price, Basket, ProductBasket
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
import csv
from django.http import HttpResponse
from django.views import View




def home(request):
    mymsg = request.GET.get('message')
    return render(request, 'home.html', {'user_message': mymsg})

class ProductFamilyList(ListView):
    model = ProductFamily

class ProductFamilyDetail(DetailView):
    model = ProductFamily  

class ProductFamilyCreate(CreateView):
    model = ProductFamily
    fields = '__all__'
    success_url = reverse_lazy('productfamily_list')

class ProductFamilyDelete(DeleteView):
    model = ProductFamily
    success_url = reverse_lazy('productfamily_list')

class ProductFamilyUpdate(UpdateView):
    model = ProductFamily
    fields = '__all__'
    success_url = reverse_lazy('productfamily_list')

class ProductList(ListView):
    model = Product

class ProductDetail(DetailView):
    model = Product

class ProductCreate(CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('product_list')

class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')

class ProductUpdate(UpdateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('product_list')


class SellingPointList(ListView):
    model = SellingPoint

class SellingPointDetail(DetailView):
    model = SellingPoint

class SellingPointCreate(CreateView):
    model = SellingPoint
    fields = '__all__'
    success_url = reverse_lazy('sellingpoint_list')

class SellingPointDelete(DeleteView):
    model = SellingPoint
    success_url = reverse_lazy('sellingpoint_list')

class SellingPointUpdate(UpdateView):
    model = SellingPoint
    fields = '__all__'
    success_url = reverse_lazy('sellingpoint_list')


class PriceList(ListView):
    model = Price

class PriceDetail(DetailView):
    model = Price

class PriceCreate(CreateView):
    model = Price
    fields = '__all__'
    success_url = reverse_lazy('price_list')

class PriceDelete(DeleteView):
    model = Price
    success_url = reverse_lazy('price_list')

class PriceUpdate(UpdateView):
    model = Price
    fields = '__all__'
    success_url = reverse_lazy('price_list')

class BasketList(ListView):
    model = Basket

class BasketDetail(DetailView):
    model = Basket

class BasketCreate(CreateView):
    model = Basket
    fields = '__all__'
    success_url = reverse_lazy('basket_list')

class BasketDelete(DeleteView):
    model = Basket
    success_url = reverse_lazy('basket_list')

class BasketUpdate(UpdateView):
    model = Basket
    fields = '__all__'
    success_url = reverse_lazy('basket_list')

class ProductBasketList(ListView):
    model = ProductBasket

class ProductBasketDetail(DetailView):
    model = ProductBasket

class ProductBasketCreate(CreateView):
    model = ProductBasket
    fields = '__all__'
    success_url = reverse_lazy('productbasket_list')

class ProductBasketDelete(DeleteView):
    model = ProductBasket
    success_url = reverse_lazy('productbasket_list')

class ProductBasketUpdate(UpdateView):
    model = ProductBasket
    fields = '__all__'
    success_url = reverse_lazy('productbasket_list')


class ProductExportCSVView(View):
    def get(self, request, *args, **kwargs):
        # Récupérer les données du modèle Product
        products = Product.objects.all()

        # Créer une réponse HTTP avec le type de contenu approprié pour un fichier CSV
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="products.csv"'

        # Créer un écrivain CSV
        writer = csv.writer(response)

        # Écrire l'en-tête du fichier CSV
        writer.writerow(['Label', 'Price Unit', 'Code', 'Product Family'])

        # Écrire les données du modèle dans le fichier CSV
        for product in products:
            writer.writerow([product.label, product.price_unit, product.code, product.productfamily.label])

        return response



from django.shortcuts import render, redirect
from django.contrib import messages
from io import StringIO

def import_product(request):
    if request.method == "POST":
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'File is not CSV type')
            return redirect("import-product")
        
        # lecture du fichier CSV
        data_set = csv_file.read().decode('UTF-8')
        io_string = StringIO(data_set)
        next(io_string)  # Ignorer l'en-tête

        for row in csv.reader(io_string, delimiter=',', quotechar='"'):
            product_family, _ = ProductFamily.objects.get_or_create(label=row[3])
            
            _, created = Product.objects.update_or_create(
                label=row[0],
                defaults={
                    'price_unit': row[1],
                    'code': row[2],
                    'productfamily': product_family,
                }
            )

        return redirect("product_list")
    
    return render(request, "app_21035/product_import.html")


def export_product_family(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="product_family_export.csv"'

    writer = csv.writer(response)
    writer.writerow(['Label'])  # En-tête du fichier CSV

    product_families = ProductFamily.objects.all()
    for product_family in product_families:
        writer.writerow([product_family.label])

    return response

def import_product_family(request):
    if request.method == "POST":
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'File is not CSV type')
            return redirect("import-product-family")
        
        data_set = csv_file.read().decode('UTF-8')
        io_string = StringIO(data_set)
        next(io_string)  # Ignorer l'en-tête

        for row in csv.reader(io_string, delimiter=',', quotechar='"'):
            _, created = ProductFamily.objects.update_or_create(
                label=row[0]
            )

        return redirect("product_family_list")
    
    return render(request, "app_21035/product_family_import.html")


class SellingPointExportCSVView(View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="sellingpoints_export.csv"'

        writer = csv.writer(response)
        writer.writerow(['Code', 'Wilaya', 'Moughataa', 'Commune', 'GPS Latitude', 'GPS Longitude'])

        sellingpoints = SellingPoint.objects.all()
        for sellingpoint in sellingpoints:
            writer.writerow([sellingpoint.code, sellingpoint.wilaya, sellingpoint.moughataa,
                             sellingpoint.commune, sellingpoint.gps_lat, sellingpoint.gps_long])

        return response

def import_selling_point(request):
    if request.method == "POST":
        csv_file = request.FILES['csv_file']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'File is not CSV type')
            return redirect('import-selling-point')

        data_set = csv_file.read().decode('UTF-8')
        io_string = StringIO(data_set)
        next(io_string)  # Ignore header

        for row in csv.reader(io_string, delimiter=',', quotechar='"'):
            _, created = SellingPoint.objects.update_or_create(
                code=row[0],
                wilaya=row[1],
                moughataa=row[2],
                commune=row[3],
                gps_lat=row[4],
                gps_long=row[5]
            )

        return redirect('selling_point_list')

    
    return render(request, 'app_21035/selling_point_import.html')


class PriceExportCSVView(View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="prices_export.csv"'

        writer = csv.writer(response)
        writer.writerow(['Value', 'Date', 'Selling Point Code', 'Product Code'])

        prices = Price.objects.all()
        for price in prices:
            writer.writerow([price.value, price.date, price.sellingpoint.code, price.product.code])

        return response


def import_price(request):
    if request.method == "POST":
        csv_file = request.FILES['csv_file']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'File is not CSV type')
            return redirect('import-price')

        data_set = csv_file.read().decode('UTF-8')
        io_string = StringIO(data_set)
        next(io_string)  # Ignore header

        for row in csv.reader(io_string, delimiter=',', quotechar='"'):
            _, created = Price.objects.update_or_create(
                value=row[0],
                date=row[1],
                sellingpoint_code=row[2],
                product_code=row[3]
            )

        return redirect('price_list')

    return render(request, 'app_21035/price_import.html')


class BasketExportCSVView(View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="baskets_export.csv"'

        writer = csv.writer(response)
        writer.writerow(['Label', 'Code', 'Description'])

        baskets = Basket.objects.all()
        for basket in baskets:
            writer.writerow([basket.label, basket.code, basket.description])

        return response

def import_basket(request):
    if request.method == "POST":
        csv_file = request.FILES['csv_file']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'File is not CSV type')
            return redirect('import-basket')

        data_set = csv_file.read().decode('UTF-8')
        io_string = StringIO(data_set)
        next(io_string)  # Ignore header

        for row in csv.reader(io_string, delimiter=',', quotechar='"'):
            _, created = Basket.objects.update_or_create(
                label=row[0],
                code=row[1],
                description=row[2]
            )

        return redirect('basket_list')

    return render(request, 'app_21035/basket_import.html')


class ProductBasketExportCSVView(View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="productbaskets_export.csv"'

        writer = csv.writer(response)
        writer.writerow(['Price ID', 'Basket ID', 'Ponderation'])

        productbaskets = ProductBasket.objects.all()
        for productbasket in productbaskets:
            writer.writerow([productbasket.price_id, productbasket.basket_id, productbasket.ponderation])

        return response

def import_product_basket(request):
    if request.method == "POST":
        csv_file = request.FILES['csv_file']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'File is not CSV type')
            return redirect('import-product-basket')

        data_set = csv_file.read().decode('UTF-8')
        io_string = StringIO(data_set)
        next(io_string)  # Ignore header

        for row in csv.reader(io_string, delimiter=',', quotechar='"'):
            _, created = ProductBasket.objects.update_or_create(
                price_id=row[0],
                basket_id=row[1],
                ponderation=row[2]
            )

        return redirect('productbasket_list')

    return render(request, 'app_21035/product_basket_import.html')