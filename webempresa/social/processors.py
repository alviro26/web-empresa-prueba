from . models import Link

def context_dict(request): #Se crea un diccionario de contexto. Contexto se abrevia como ctx
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url
    return ctx