from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.utils.translation import ugettext as _
from .models import devis


def is_email(email):
    import re
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    return re.search(regex, email)


def is_phone(email):
    import re
    regex = '^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$'
    return re.search(regex, email)


def splitUrl(request):
    return [request.path.split("/"), len(request.path.split("/"))]


def send_email_template(mail_information, template, context):
    msg = EmailMultiAlternatives(
        subject=mail_information['subject'],
        body=mail_information['body'],
        from_email=mail_information['from_email'],
        to=mail_information['to'])
    html_template = get_template("pages/{}".format(template)).render(context)
    msg.attach_alternative(html_template, "text/html")
    return msg


class myForm():
    def __init__(self, max_length, constraint=None, text='', alias='nvhvh'):
        if constraint is None:
            constraint = {}
        self.constraint = constraint
        self.max_length = max_length
        self.text = text
        self.alias = alias

    def is_valid(self):
        if self.constraint == {}:
            if not len(self.text) < self.max_length:
                return {'status': False, 'msg': [
                    _('Le text saisie dans le champs possède un tros grand nombre de caractère la taille maximale est '
                      '{} caractères'.format(
                        self.max_length))]}
            else:
                return {'status': True, 'msg': []}
        else:
            result = {'status': True, 'msg': []}
            if 'required' in self.constraint:
                if not len(self.text) > 0:
                    result['status'] = False
                    result['msg'].append(self.constraint['required'])
            if 'email' in self.constraint:
                if not is_email(self.text):
                    result['status'] = False
                    result['msg'].append(self.constraint['email'])
            if 'number' in self.constraint:
                if not is_phone(self.text) and self.text != '':
                    result['status'] = False
                    result['msg'].append(self.constraint['number'])
            if self.max_length < len(self.text):
                result['status'] = False
                result['msg'].append(
                    _('Le text saisie dans le champs possède un très grand nombre de caractère la taille maximale est '
                      '{} caractères'.format(
                        self.max_length)))
            return result

    def get_attrib(self):
        return self.__dict__


class form():
    def is_valid(self):
        messages = {item: key.is_valid() for item, key in self.__dict__.items()}
        errors = {}
        for key, value in messages.items():
            if not value['status']:
                errors[key] = value['msg']
        return errors


class contactForm(form):
    def __init__(self, post):
        self.name = myForm(max_length=100, constraint={'required': _('Ce champs est obligatoire')}, text=post['name'])
        self.email = myForm(max_length=100,
                            constraint={'email': _('Adresse mail invalid respecter le format : test@test.test !'),
                                        'required': _('Ce champs est obligatoire')},
                            text=post['email'])
        self.phone = myForm(max_length=100, constraint={
            'number': _('Veuillez saisir un numéro de téléphone valide au format +(XXX)XXXXXXXX..')},
                            text=post['phone'])
        self.company = myForm(max_length=100,
                              text=post['company'])
        self.message = myForm(max_length=100, constraint={'required': _('Ce champs est obligatoire')},
                              text=post['message'])


class devisForm(form):
    def __init__(self, post):
        self.name = myForm(max_length=100, constraint={'required': _('Ce champs est obligatoire')}, text=post['name'])
        self.email = myForm(max_length=100,
                            constraint={'email': _('Adresse mail invalid respecter le format : test@test.test !'),
                                        'required': _('Ce champs est obligatoire')},
                            text=post['email'])
        self.phone = myForm(max_length=100, constraint={
            'number': _('Veuillez saisir un numéro de téléphone valide au format +(XXX)XXXXXXXX..')},
                            text=post['phone'])
        self.info_supp = myForm(max_length=100,
                                text=post['info_supp'])
        self.date_expedition = myForm(max_length=100,
                                      text=post['date_expedition'])
        self.transport_mode = myForm(max_length=100,
                                     text=post.getlist('transport_mode'))
        self.livraison = myForm(max_length=100, constraint={'required': _('Ce champs est obligatoire')},
                                text=post['livraison'])
        self.livraison_country = myForm(max_length=100, constraint={'required': _('Ce champs est obligatoire')},
                                        text=post['livraison_country'])
        self.dimension = myForm(max_length=100,
                                text=post['dimension'])
        self.type_emballage = myForm(max_length=100,
                                     text=post['type_emballage'])
        self.volume = myForm(max_length=100, constraint={'required': _('Ce champs est obligatoire')},
                             text=post.get('volume', ''))
        self.volume_unite = myForm(max_length=100, constraint={'required': _('Ce champs est obligatoire')},
                                   text=post['volume_unite'])
        self.poids = myForm(max_length=100, constraint={'required': _('Ce champs est obligatoire')}, text=post['poids'])
        self.poids_unite = myForm(max_length=100, constraint={'required': _('Ce champs est obligatoire')},
                                  text=post.get('poids_unite', ''))
        self.marchandise = myForm(max_length=100, constraint={'required': _('Ce champs est obligatoire')},
                                  text=post['marchandise'])
        self.lieu_enlevement = myForm(max_length=100, constraint={'required': _('Ce champs est obligatoire')},
                                      text=post['lieu_enlevement'])
        self.enlevement_country = myForm(max_length=100, constraint={'required': _('Ce champs est obligatoire')},
                                         text=post['enlevement_country'])

    def getmodel(self):
        return devis(
            name=self.name.text,
            email=self.email.text,
            phone=self.phone.text,
            info_supp=self.info_supp.text,
            date_expedition=self.date_expedition.text,
            transport_mode=self.transport_mode.text,
            livraison=self.livraison.text,
            livraison_country=self.livraison_country.text,
            dimension=self.dimension.text,
            type_emballage=self.type_emballage.text,
            volume=self.volume.text,
            volume_unite=self.volume_unite.text,
            poids=self.poids.text,
            poids_unite=self.poids_unite.text,
            marchandise=self.marchandise.text,
            lieu_enlevement=self.lieu_enlevement.text,
            enlevement_country=self.enlevement_country.text,

        )
