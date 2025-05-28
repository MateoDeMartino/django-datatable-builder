from django.template.loader import render_to_string

def datatables(request, datatable=None):
    if datatable:
        if not "order" in datatable.keys():
            datatable["order"] = [0, "asc"]
        if not "responsive" in datatable.keys():
            # Por defecto usa barra horizontal para tablas, si se cambia a true hace columns autohide
            datatable["responsive"] = "false"

        return render_to_string("datatable.html", datatable, request=request)
    return None