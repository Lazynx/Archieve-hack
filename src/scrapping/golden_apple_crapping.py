import requests
import json

def get_golden_apple_products(page_number: int):
    cookies = {
    'ga-device-id': 'j6aEZURFyNcO8eOadzh35',
    'mindboxDeviceUUID': 'c71134d6-790c-4ced-9bcd-bbf577ad8aea',
    'directCrm-session': '%7B%22deviceGuid%22%3A%22c71134d6-790c-4ced-9bcd-bbf577ad8aea%22%7D',
    'advcake_track_id': '3fd85bb4-bbd4-4e97-8105-a440b5b2d115',
    'advcake_session_id': 'd7ba86b5-170d-0aef-9492-b500ab78d010',
    '_gcl_au': '1.1.8993364.1723630724',
    'tmr_lvid': 'e4832f18f97548b52320e70af930b43d',
    'tmr_lvidTS': '1723630724596',
    '_ym_uid': '1723630725758993112',
    '_ym_d': '1723630725',
    'welcome-modal': 'card_acquired',
    'access_token': 'eyJhbGciOiJSUzI1NiIsImtpZCI6IkE4QTdDRDBFNjE0REQxNzE1OTU0ODZCNjA5MjNDMTBCRDYyMDZGMTRSUzI1NiIsInR5cCI6ImF0K2p3dCIsIng1dCI6InFLZk5EbUZOMFhGWlZJYTJDU1BCQzlZZ2J4USJ9.eyJuYmYiOjE3MjM3MjM5NTYsImV4cCI6MTc1NTI1OTk1NiwiaXNzIjoiaHR0cHM6Ly9wbGFpZC5nb2xkYXBwbGUua3oiLCJhdWQiOiJJbnRlcm5hbEFQSSIsImNsaWVudF9pZCI6ImNsaWVudF93ZWIiLCJzdWIiOiI3Nzc2NzMwMTkwMyIsImF1dGhfdGltZSI6MTcyMzcyMzk1NiwiaWRwIjoicGhvbmVfc21zX3Rva2VuIiwibWFnZW50b19pZCI6Ijg3NDkxODIiLCJjdXN0b21lcl9pZCI6IjExOTRiYmZmLWNiYmEtNGE1NS05ODNjLTBhNGI4NDQxOGJkNiIsImN1c3RvbWVyX3Bob25lIjoiNzc3NjczMDE5MDMiLCJjdXN0b21lcl9pc19yZWdpc3RlcmVkIjoiMCIsImN1c3RvbWVyX2dyb3VwX2lkIjoiMCIsImp0aSI6Ijk1OTU0RTdFRkM5OTlFM0VFNTUxODlBNjE4NDA1QjVFIiwiaWF0IjoxNzIzNzIzOTU2LCJzY29wZSI6WyJvcGVuaWQiLCJwcm9maWxlIiwiV2ViQVBJIiwib2ZmbGluZV9hY2Nlc3MiXX0.DWrGmGPYYNS1YM9okuGjN7rUbVwGXTxt2gOzcQKDoblnVrA-OCk6M-6vZgvkUxorTh_Eu0umREcWM9Jh_XKnCl536xpkxQHteu_gC5bU3F555oi-6M9kpTYOoC4DdlzvL9AYqafe8ntTjzAPMAlO0CpeHo9IY1NPiVYga6rRMOkKvoUfR46uqFya7S9trUp0y0CjoZTu9BhQ9KgSun9UVsZUy-uaED0M-k5eMhHiGc2X6FuVx3HleSgJAcO894cCpwfD1ceqlkX8uTE7ZRaL9_u1bVCIdjczsVLQ5vF9OoBHlgCSFgUUzm7TSQax4nj8QVIhUSNzPaVkAdedm4A-5h_qbIzEGHMPXz-XmFUtQhHR12_zv7dMVE_VmAWNDn0mc0UWYAqYte8rPP585ZNYJrWNReEMV0K-7lFBtbrEUVGaPrvWTpZXZYDm-n_YWiiwRt-EvwaeXY3FQ0HXU0Ex3XQ1aDC3J1TwS8DwdCG_82DeXduYoNRlcM2p_GPCCHvSFkDR44bVA6YGuTXDPlWarwy-uoprpxPbDugIkjrmWr7pUTngO9cxcPYkc9ex_zN0OlUObjdimWGYp0AGlQC_Ut3nK4l8a8zB1HZH4NgDCKPe82PenUSdGB13q_Afq5gcCTpIOzUjlIiB89pKOy0QxZzW6LiTOmoU9uNJHpc4GZY',
    'has_access_token': 'true',
    'refresh_token': '0457DAB337CEA4BB1D2530B4D458087FDC7AE3133D0FE5E7FEB8F7DB5AB9FE2C',
    'has_refresh_token': 'true',
    'X-Magento-Vary': '81c72af773c561b16e2d83c6d8dc2fd72c09d694',
    'userId': '8749182',
    'MCS_SESSID': '7e664133c407989333824f4ebea156bf',
    'ga-lang': 'ru',
    'client-store-code': 'kz',
    'digi-analytics-sessionId': 'Yb83czXWdibV2h4MwEdKR',
    'ga-location-city-id': 'ChIJq8vFFn1ugzgRdm2YrY9mRD0',
    '_gid': 'GA1.2.468199576.1725966732',
    '_ym_visorc': 'b',
    '_ym_isad': '2',
    'domain_sid': 'A_XPl_VhZMsozrjOIPLyl%3A1725966732772',
    '_ga_QE5MQ8XJJK': 'GS1.1.1725966732.13.1.1725966775.0.0.0',
    '_ga': 'GA1.1.1653912085.1723630724',
    '_spx': 'eyJpZCI6ImQ5Mjc0MmY2LTQ5Y2QtNGFjZC04MzRlLTIwYTM0YzZhOTQwMSIsImZpeGVkIjp7InN0YWNrIjpbMCwwXX19',
    'advcake_track_url': '%3D202409093JzyjycY8v9453Iqfm%2FP7yqf4Nn6DDymBFuigHBdwbG%2B1%2BgYsCO6C8HDRy4Nc0I3%2BTHNnUYkTzZJBkNFxySECnz0KpwanfcqXiJ%2FqI6aesPjT%2FHXS6E4bcouj2Q2wEnDm75nbY92y%2BD1aidCUylFIeVmGpqovsHIluBPXrzy6bh8%2FBtNYpdUlHss5jvJG21ovjYrj%2FRhwKQJoCwM%2FPd8nyf%2BaLqTiaNte8LRGaFa9fNtJbUKqNJw67Hig2nRn1Dbd%2FhmE8QZfzmkCel5OMi0QM%2BWaLgCsfEZQtIWg5Mno3pQ6vVhUbVYWbNxVTHsf44fwm3g6ghDIdZAT8yW7OrAJDsnbIjY82h1CEbp2tCKqo%2BCBidp8t42zZq%2Frxn8l6tWiGzbDCzPxBhyLVJcofO8pnQKTm4OuSXAqNKA0SM%2BmZW%2BwKu%2F09oY8MXGHU5sP3cluqcatAaSHFxMOImNR67576RcC08yuUZsitHsV5nckJ%2Fph%2FnyKytrAK2A6R5nOGI2VtxTqjn%2FAk7ZQJe9koU70ib5%2B3tJeQUbZAmeR4KGlFDJ31ZjjZpgoeYtoJ9jtVGTWZ1OGxX6Xl%2FhIbKwazTnjihIDIYpQrufL3PYbafzcyWWriO6m2KLEnBtitzKdSC8dAo6818LpHHSm8%2F7nMwk1kIgg9CV0z8xYwhmra3CFluSL5Txfvu3oz8%3D',
    'section_data_ids': '%7B%22geolocation%22%3A1725966776%2C%22adult_goods%22%3A1725966775%2C%22cart%22%3A1725966776%7D',
    'tmr_detect': '0%7C1725966777545',
    }

    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru,en;q=0.9',
    # 'cookie': 'ga-device-id=j6aEZURFyNcO8eOadzh35; mindboxDeviceUUID=c71134d6-790c-4ced-9bcd-bbf577ad8aea; directCrm-session=%7B%22deviceGuid%22%3A%22c71134d6-790c-4ced-9bcd-bbf577ad8aea%22%7D; advcake_track_id=3fd85bb4-bbd4-4e97-8105-a440b5b2d115; advcake_session_id=d7ba86b5-170d-0aef-9492-b500ab78d010; _gcl_au=1.1.8993364.1723630724; tmr_lvid=e4832f18f97548b52320e70af930b43d; tmr_lvidTS=1723630724596; _ym_uid=1723630725758993112; _ym_d=1723630725; welcome-modal=card_acquired; access_token=eyJhbGciOiJSUzI1NiIsImtpZCI6IkE4QTdDRDBFNjE0REQxNzE1OTU0ODZCNjA5MjNDMTBCRDYyMDZGMTRSUzI1NiIsInR5cCI6ImF0K2p3dCIsIng1dCI6InFLZk5EbUZOMFhGWlZJYTJDU1BCQzlZZ2J4USJ9.eyJuYmYiOjE3MjM3MjM5NTYsImV4cCI6MTc1NTI1OTk1NiwiaXNzIjoiaHR0cHM6Ly9wbGFpZC5nb2xkYXBwbGUua3oiLCJhdWQiOiJJbnRlcm5hbEFQSSIsImNsaWVudF9pZCI6ImNsaWVudF93ZWIiLCJzdWIiOiI3Nzc2NzMwMTkwMyIsImF1dGhfdGltZSI6MTcyMzcyMzk1NiwiaWRwIjoicGhvbmVfc21zX3Rva2VuIiwibWFnZW50b19pZCI6Ijg3NDkxODIiLCJjdXN0b21lcl9pZCI6IjExOTRiYmZmLWNiYmEtNGE1NS05ODNjLTBhNGI4NDQxOGJkNiIsImN1c3RvbWVyX3Bob25lIjoiNzc3NjczMDE5MDMiLCJjdXN0b21lcl9pc19yZWdpc3RlcmVkIjoiMCIsImN1c3RvbWVyX2dyb3VwX2lkIjoiMCIsImp0aSI6Ijk1OTU0RTdFRkM5OTlFM0VFNTUxODlBNjE4NDA1QjVFIiwiaWF0IjoxNzIzNzIzOTU2LCJzY29wZSI6WyJvcGVuaWQiLCJwcm9maWxlIiwiV2ViQVBJIiwib2ZmbGluZV9hY2Nlc3MiXX0.DWrGmGPYYNS1YM9okuGjN7rUbVwGXTxt2gOzcQKDoblnVrA-OCk6M-6vZgvkUxorTh_Eu0umREcWM9Jh_XKnCl536xpkxQHteu_gC5bU3F555oi-6M9kpTYOoC4DdlzvL9AYqafe8ntTjzAPMAlO0CpeHo9IY1NPiVYga6rRMOkKvoUfR46uqFya7S9trUp0y0CjoZTu9BhQ9KgSun9UVsZUy-uaED0M-k5eMhHiGc2X6FuVx3HleSgJAcO894cCpwfD1ceqlkX8uTE7ZRaL9_u1bVCIdjczsVLQ5vF9OoBHlgCSFgUUzm7TSQax4nj8QVIhUSNzPaVkAdedm4A-5h_qbIzEGHMPXz-XmFUtQhHR12_zv7dMVE_VmAWNDn0mc0UWYAqYte8rPP585ZNYJrWNReEMV0K-7lFBtbrEUVGaPrvWTpZXZYDm-n_YWiiwRt-EvwaeXY3FQ0HXU0Ex3XQ1aDC3J1TwS8DwdCG_82DeXduYoNRlcM2p_GPCCHvSFkDR44bVA6YGuTXDPlWarwy-uoprpxPbDugIkjrmWr7pUTngO9cxcPYkc9ex_zN0OlUObjdimWGYp0AGlQC_Ut3nK4l8a8zB1HZH4NgDCKPe82PenUSdGB13q_Afq5gcCTpIOzUjlIiB89pKOy0QxZzW6LiTOmoU9uNJHpc4GZY; has_access_token=true; refresh_token=0457DAB337CEA4BB1D2530B4D458087FDC7AE3133D0FE5E7FEB8F7DB5AB9FE2C; has_refresh_token=true; X-Magento-Vary=81c72af773c561b16e2d83c6d8dc2fd72c09d694; userId=8749182; MCS_SESSID=7e664133c407989333824f4ebea156bf; ga-lang=ru; client-store-code=kz; digi-analytics-sessionId=Yb83czXWdibV2h4MwEdKR; ga-location-city-id=ChIJq8vFFn1ugzgRdm2YrY9mRD0; _gid=GA1.2.468199576.1725966732; _ym_visorc=b; _ym_isad=2; domain_sid=A_XPl_VhZMsozrjOIPLyl%3A1725966732772; _ga_QE5MQ8XJJK=GS1.1.1725966732.13.1.1725966775.0.0.0; _ga=GA1.1.1653912085.1723630724; _spx=eyJpZCI6ImQ5Mjc0MmY2LTQ5Y2QtNGFjZC04MzRlLTIwYTM0YzZhOTQwMSIsImZpeGVkIjp7InN0YWNrIjpbMCwwXX19; advcake_track_url=%3D202409093JzyjycY8v9453Iqfm%2FP7yqf4Nn6DDymBFuigHBdwbG%2B1%2BgYsCO6C8HDRy4Nc0I3%2BTHNnUYkTzZJBkNFxySECnz0KpwanfcqXiJ%2FqI6aesPjT%2FHXS6E4bcouj2Q2wEnDm75nbY92y%2BD1aidCUylFIeVmGpqovsHIluBPXrzy6bh8%2FBtNYpdUlHss5jvJG21ovjYrj%2FRhwKQJoCwM%2FPd8nyf%2BaLqTiaNte8LRGaFa9fNtJbUKqNJw67Hig2nRn1Dbd%2FhmE8QZfzmkCel5OMi0QM%2BWaLgCsfEZQtIWg5Mno3pQ6vVhUbVYWbNxVTHsf44fwm3g6ghDIdZAT8yW7OrAJDsnbIjY82h1CEbp2tCKqo%2BCBidp8t42zZq%2Frxn8l6tWiGzbDCzPxBhyLVJcofO8pnQKTm4OuSXAqNKA0SM%2BmZW%2BwKu%2F09oY8MXGHU5sP3cluqcatAaSHFxMOImNR67576RcC08yuUZsitHsV5nckJ%2Fph%2FnyKytrAK2A6R5nOGI2VtxTqjn%2FAk7ZQJe9koU70ib5%2B3tJeQUbZAmeR4KGlFDJ31ZjjZpgoeYtoJ9jtVGTWZ1OGxX6Xl%2FhIbKwazTnjihIDIYpQrufL3PYbafzcyWWriO6m2KLEnBtitzKdSC8dAo6818LpHHSm8%2F7nMwk1kIgg9CV0z8xYwhmra3CFluSL5Txfvu3oz8%3D; section_data_ids=%7B%22geolocation%22%3A1725966776%2C%22adult_goods%22%3A1725966775%2C%22cart%22%3A1725966776%7D; tmr_detect=0%7C1725966777545',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "YaBrowser";v="24.7", "Yowser";v="2.5"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-9c3b67b1604ea5f47f8cc715cf0de706-771142f0ddebf214-01',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 YaBrowser/24.7.0.0 Safari/537.36',
    'x-app-version': '1.51.0',
    'x-gast': '36934996.83679548,36934996.83679548',
    }
    params = {
        'categoryId': '3000000007',
        'cityId': 'ChIJq8vFFn1ugzgRdm2YrY9mRD0',
        'pageNumber': str(page_number),
        'customerGroupId': '18',
    }

    response = requests.get('https://goldapple.kz/front/api/catalog/products', params=params, cookies=cookies, headers=headers)
    with open('golden_apple.json', 'x') as f:
        json.dump(response.json(), f, indent=4)
        
    return response.json()
    

get_golden_apple_products(1)

