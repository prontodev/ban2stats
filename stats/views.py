from django.http.response import HttpResponse
from stats.packages.attacked_service import AttackedServicePackageBuilder
from stats.packages.blocked_country import BlockedCountryPackageBuilder
from stats.packages.blocked_location import BlockedLocationPackageBuilderMinimized


def return_json_content(content):
    response = HttpResponse(content, content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"
    return response


def get_attacked_services(request):
    content = AttackedServicePackageBuilder().render_all_objects_as_list()
    return return_json_content(content)


def get_blocked_countries(request):
    content = BlockedCountryPackageBuilder().render_all_objects_as_list()
    return return_json_content(content)


def get_block_locations(request):
    content = BlockedLocationPackageBuilderMinimized().render_all_objects_as_list()
    return return_json_content(content)


def get_location_details(request):
    # content = LocationDetailsPackageBuilder().render()
    content = """
    [{
    "service_name": "Wordpress Portal",
    "ip" : "202.99.83.24",
    "last_seen": "2014-10-22 04:53:06.533996+00:00",
    "ban_count": 200
    }]
    """
    return return_json_content(content)