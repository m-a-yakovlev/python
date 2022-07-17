import requests
import folium

def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        #print(response)

        data = {
            '[IP]' : response.get('query'),
            '[Country]' : response.get('country'),
            '[City]' : response.get('city'),
            '[Lat]' : response.get('lat'),
            '[Lon]' : response.get('lon')
        }

        for k, v in data.items():
            print(f'{k} : {v}')


        area = folium.Map(location=[data['[Lat]'], data['[Lon]']])
        area.save(f'{response.get("query")}_{response.get("city")}.html')



    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection!')




def main():
    ip = input('Please enter IP address: ')
    get_info_by_ip(ip=ip)



if __name__ == "__main__":
    main()