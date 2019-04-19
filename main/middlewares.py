from .models import SubrRubric

def bboard_context_processor(request):
    context = {}
    context['rubrics'] = SubrRubric.objects.all()

    return context
