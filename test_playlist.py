import playlist
import requests
import json


app = playlist.app.test_client()


def test_website():
    payload = {
        "url": 'http://www.radiomirchi.com/thiruvananthapuram/countdown/malayalam-top-20',
        "settings": {
            "parser": "html5lib",
            "headers": {
                "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:19.0) Gecko/20100101 Firefox/19.0",
            }
        },
        "soup_path_for_list": {
            "tag": "div",
            "attr": {
                "class": "mirchi_20_box2"
            }
        },
        "soup_path_for_keyword": {
            "paths": [
                {
                    "tag": "span",
                    "attr": {
                        "class": "or12"
                    }
                },
                {
                    "tag": "span",
                    "attr": {
                        "class": "moviename"
                    }
                },
            ]
        }
    }
    rv = app.post('/', data=dict(data=json.dumps(payload)))
    expected_data = "MARIVIL  DRISHYAM,KAATTU MOOLIYO OM SHANTHI OSANA ,OLANJAALI KURUVIL 1983,EERAN KAATTIN  SALALA MOBILES,MANDARAME OM SHANTHI OSANA ,KANNADI VATHIL LONDON BRIDGE,OMANA POOVE ORU INDIAN PRANAY...,RASOOL ALLAH SALALA MOBILES,PUNCHIRI THANCHUM BYCYCLE THIEVES,LA LA LASA SALALA MOBILES,AASHICHAVAN PUNYALAN AGARBATTIS,NENJILE NENJILE 1983,THAMARAPOONKAVANAT... BALYAKALA SAKHI,CHEMMANA CHELORUKKI MANNAR MATHAI SPE...,THALAVATTOM 1983,THIRIYAANE MANNAR MATHAI SPE...,MADHUMATHI GEETHANJALI,CHINNI CHINNI LONDON BRIDGE,THEERATHE NEELUNNE THIRA,OTTEKKU PAADUNNA NADAN"
    assert rv.data == expected_data