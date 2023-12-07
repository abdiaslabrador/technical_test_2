from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from bs4 import BeautifulSoup


# Create your views here.
class get_api(APIView):
    def get(self, request, format=None):
        if request.GET.get("date"):
            list_chart = request.GET.get("date").split(sep="-")
            array = [int(i) for i in list_chart]
            day = int(array[0])
            month = int(array[1])
            year = int(array[2])
            if year < 2013:
                return Response(
                    "fecha no válida, fecha mínima es 01-01-2013", status=404
                )

            r = requests.get(f"https://www.sii.cl/valores_y_fechas/uf/uf{year}.htm")
            id_month = ""
            if month == 12:
                id_month = "mes_diciembre"
            elif month == 11:
                id_month = "mes_noviembre"
            elif month == 10:
                id_month = "mes_octubre"
            elif month == 9:
                id_month = "mes_septiembre"
            elif month == 8:
                id_month = "mes_agosto"
            elif month == 7:
                id_month = "mes_julio"
            elif month == 6:
                id_month = "mes_junio"
            elif month == 5:
                id_month = "mes_mayo"
            elif month == 4:
                id_month = "mes_abril"
            elif month == 3:
                id_month = "mes_marzo"
            elif month == 2:
                id_month = "mes_febrero"
            elif month == 1:
                id_month = "mes_enero"
            soup = BeautifulSoup(r.content, "html.parser")
            results = soup.find(id=id_month).find("table")
            rows = results.tbody.find_all("tr")

            ban = False
            th_count = 0
            td_array = []
            for row in rows[1:]:
                for th in row.find_all("th"):
                    if th.string == str(day):
                        ban = True
                        break
                    else:
                        th_count = th_count + 1

                for td in row.find_all("td"):
                    td_array.append(td.string)
                if ban:
                    break
            fomento = td_array[th_count]
            return Response(
                {"fecha": f"{day}-{month}-{year}", "fomento": fomento}, status=200
            )
        else:
            return Response("No hay fecha pasada por parametros", status=404)
