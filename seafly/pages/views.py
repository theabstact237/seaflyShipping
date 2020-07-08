from django.conf import settings
from django.shortcuts import render
import markdown2
from django.shortcuts import redirect
from pages.models import Pages, contact as Contact
from .utils import contactForm, splitUrl, devisForm, send_email_template
from django.db.models import Q


def getPageDB(request, pagename):
    urlsplit = splitUrl(request)
    try:
        if "promos" in urlsplit[0]:
            page = Pages.objects.get(name="promos/" + pagename)
            url = "pages/page-promos.html"
        elif "faq" in urlsplit[0]:
            page = Pages.objects.get(name="faq/" + pagename)
            url = "pages/page.html"
        else:
            page = Pages.objects.get(name=pagename)
            url = "pages/page.html"
    except:
        return redirect("/")

    switcher = {
        'fr': [page.title, page.content],
        'en': [page.title_en, page.content_en],
        'th': [page.title_th, page.content_th],
    }
    page.title = switcher.get(request.LANGUAGE_CODE, '')[0]
    page.content = switcher.get(request.LANGUAGE_CODE, '')[1]
    page.content = markdown2.markdown(page.content)
    context = {
        'page': page
    }
    return render(request, url, context)


def getPages(request):
    paths = splitUrl(request)[0]
    lenght = splitUrl(request)[1]
    page = paths[lenght - 1] if paths[lenght - 1] != '' else 'index'
    return render(request, "pages/{}.html".format(page))


def getContact(request):
    context = {}
    if request.POST:
        form = contactForm(request.POST)
        errors = form.is_valid()
        post = request.POST
        if not errors == {}:
            context = {
                "errors": errors,
                "post": post,
            }
        else:
            contact = Contact(name=post['name'], email=post['email'], phone=post['phone'], company=post['company'],
                              message=post['message'])
            contact.save()
            subject = "Soumission du formulaire de contact"
            from_mail = settings.EMAIL_HOST_USER
            to_list = ['mevaajules2@gmail.com', settings.EMAIL_HOST_USER]
            post._mutable = True
            mail_informations = {
                'subject': subject,
                'body': 'ok',
                'from_email': from_mail,
                'to': to_list
            }
            context_template = {
                'post': post
            }
            send_email_template(mail_informations, 'email_contact.html', context_template).send()
            success = "Enregistrement effectué avec succes"
            context = {
                "success": success
            }
    return render(request, "pages/contact.html", context)


def getDevis(request):
    context = {}
    if request.POST:
        form = devisForm(request.POST)
        errors = form.is_valid()
        post = request.POST
        if not errors == {}:
            context = {
                "errors": errors,
                "post": post,
                "mode": post.getlist('transport_mode'),
            }
        else:
            form.getmodel().save()
            subject = "Demande de devis"
            from_mail = settings.EMAIL_HOST_USER
            to_list = ['mevaajules2@gmail.com', settings.EMAIL_HOST_USER]
            post._mutable = True
            mail_informations = {
                'subject': subject,
                'body': 'ok',
                'from_email': from_mail,
                'to': to_list
            }
            post['transport_mode'] = ', '.join(post.getlist('transport_mode'))
            print(post.getlist('transport_mode'))
            context_template = {
                'post': post
            }
            send_email_template(mail_informations, 'email_devis.html', context_template).send()
            context['success'] = 'Demande de devis enregistrée avec succès'

    return render(request, "pages/devis.html", context)


def search(request):
    if request.GET and request.GET['q']:
        q = request.GET['q']
        pages = Pages.objects.filter(
            Q(title__contains=q) |
            Q(title_en__contains=q) |
            Q(title_th__contains=q) |
            Q(content__contains=q) |
            Q(content_en__contains=q) |
            Q(content_th__contains=q)
        )
        context = {
            'results': pages,
            'query': q,
            'ln': request.LANGUAGE_CODE
        }
        return render(request, "pages/search.html", context)
    else:
        return redirect("/")