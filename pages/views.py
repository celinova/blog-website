from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Entry


def entries_index(request):
    entries = Entry.objects.all()
    return render(request, "entries_index.html", {"entries_index": entries})


def entry_view(request, entry):
    entry_data = get_object_or_404(Entry, entry_title=entry)
    return render(request, "entry_template.html", {"entry_data": entry_data})


@login_required
def add_entry(request):
    # retrieve data from the "add page" form
    if request.method == "POST":
        input_title = str(request.POST.get("title_field"))
        input_body = str(request.POST.get("body_field"))

        # check for title collisions, not super inclined to do this by id ;P
        if input_title in Entry.objects.all():
            return render(
                request, "entry_already_exists.html", {"input_title": input_title}
            )
        else:
            created_entry = Entry.objects.create(
                entry_title=input_title,
                entry_text=input_body,
                publish_date=timezone.now(),
            )
            return render(request, "entry_added.html", {"created_entry": created_entry})


# @login_required
# def edit_entry(request):
#     if request.method == "POST":
#         return render()


@login_required
def remove_entry(request, entry):
    entry_data = get_object_or_404(Entry, entry_title=entry)
    entry_data.delete()
    return render(request, "entry_deleted.html", {"entry": entry_data})
