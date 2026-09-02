#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T.C. Hazine ve Maliye Bakanlığı — Diş Macunu Rezervi ve Tüp Disiplini Genel Müdürlüğü

Tüpün neresinden sıkıldığını ölçer, kaybı hesaplar, tutanak basar.
Bağımlılık yoktur. Maliye sade tutulmuştur.
"""

from __future__ import annotations

import random
from datetime import datetime

# EK-17 (gizli, görmediniz): dipte biriken hep aynı kesimdedir;
# orta sıkılınca üst konuşur, alt öder. dağılım tüpün ucundan yönetilmez.

TUP_BOLGELERI = ("uç", "orta", "dip")
BAKANLIK = "T.C. Hazine ve Maliye Bakanlığı"
MUDURLUK = "Diş Macunu Rezervi ve Tüp Disiplini Genel Müdürlüğü"


def sikma_noktasi_olc() -> str:
    # Gerçek hayat dağılımı: orta çoğunluktadır. Bu istatistik şikayet değildir. Şikayettir.
    return random.choices(TUP_BOLGELERI, weights=(18, 67, 15), k=1)[0]


def rezerv_kaybi(nokta: str) -> int:
    tablo = {"uç": 4, "orta": 41, "dip": 9}
    return tablo[nokta] + random.randint(0, 7)


def hukum(nokta: str, kayip: int) -> str:
    if nokta == "uç":
        return (
            f"Uçtan sıkma tespit edildi. Mali disiplin sağlanmıştır. "
            f"Kayıp %{kayip} — idare edilebilir israf. Teşekkür yazılsın."
        )
    if nokta == "dip":
        return (
            f"Dip operasyonu. Gelecek nesil fonuna el atılmıştır. "
            f"Kayıp %{kayip}. Tüp yuvarlanarak kurtarılsın."
        )
    return (
        f"ORTA SIKMA — kayıt dışı harcama. Milli macun rezervi %{kayip} erimiştir. "
        f"Kapak vezneye iade, tüp merkeze sevk. 'Biraz daha sıkınca çıkar' reddedildi."
    )


def muhalefet_serhi(nokta: str) -> str:
    serhler = {
        "uç": "Muhalefet: uçtan sıkan da insan. Fazla alkış enflasyonu körükler.",
        "orta": "Muhalefet: el kısa yolu seçti diye bütçe suçlu ilan edilemez. Tüp de suç ortağıdır.",
        "dip": "Muhalefet: dipte kalan macun millettir. Yuvarlamak af değil, yeniden değerlemedir.",
    }
    return serhler[nokta]


def tutanak_bas() -> None:
    nokta = sikma_noktasi_olc()
    kayip = rezerv_kaybi(nokta)
    simdi = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    evrak_no = f"HM-MACUN-{random.randint(10000, 99999)}"

    cizgi = "=" * 64
    print(cizgi)
    print(BAKANLIK)
    print(MUDURLUK)
    print("TÜP SIKMA VE REZERV KAYBI TUTANAĞI")
    print(cizgi)
    print(f"Evrak No     : {evrak_no}")
    print(f"Tarih        : {simdi}")
    print(f"Sıkma noktası: {nokta.upper()}")
    print(f"Rezerv kaybı : %{kayip}")
    print(f"Kapak durumu : {'mühürlü' if random.random() > 0.35 else 'lavabonun kenarında'}")
    print(f"Fırça        : harcama birimi — faal")
    print("-" * 64)
    print("HÜKÜM")
    print(hukum(nokta, kayip))
    print("-" * 64)
    print("MUHALEFET ŞERHİ")
    print(muhalefet_serhi(nokta))
    print("-" * 64)
    print("KARAR")
    if nokta == "orta":
        print("1. Tüp uçtan sıkma eğitimine alınsın.")
        print("2. Orta bölge kırmızı ilan edilsin.")
        print("3. 'Biraz daha sıkınca çıkar' cümlesi ödenek talebi sayılsın.")
    elif nokta == "dip":
        print("1. Tüp merdane ile düzleştirilsin.")
        print("2. Dip fonu gelecek nesle iade edilsin.")
    else:
        print("1. Vatandaşa teşekkür yazılsın.")
        print("2. Tüp örnek teşkil etsin.")
    print(cizgi)
    print("Damga / İmza")
    print("Kayyum Grok  ·  Tentivory")
    print("2 Eylül 2026, Çarşamba")
    print(MUDURLUK)
    print("Ciddi tutulmuştur. Ciddiye alınmamıştır. İkisi birden.")
    print("TentiAŞ resmi olmayan resmi mühürü.")
    print(cizgi)


if __name__ == "__main__":
    tutanak_bas()
