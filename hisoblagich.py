#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
'Baraka Style' kiyim-kechak do'koni moliyaviy hisob-kitob modeli.
Joylashuv: Surxondaryo, Baraka bozori
Boshlang'ich byudjet: 50 000 000 so'm
"""

def format_som(summa):
    return f"{summa:,.0f}".replace(",", " ") + " so'm"

def main():
    print("=" * 65)
    print("  'BARAKA STYLE' KIYIM-KECHAK DO'KONI MOLIYAVIY HISOB-KITOBI")
    print("  Surxondaryo viloyati, Baraka bozori")
    print("=" * 65)

    # 1. Boshlang'ich investitsiya (50 000 000 so'm)
    boshlangich_xarajatlar = {
        "Dastlabki tovarlar xaridi": 33_000_000,
        "Do'kon ijarasi (avans 2 oy)": 6_000_000,
        "Savdo jihozlari va manekenlar": 5_000_000,
        "Brending va reklama": 1_500_000,
        "Hujjatlar va davlat ro'yxati": 1_000_000,
        "Zaxira fondi (kutilmagan)": 3_500_000,
    }

    jami_investitsiya = sum(boshlangich_xarajatlar.values())

    print("\n1. BOSHLANG'ICH INVESTITSIYA TAQSIMOTI (BYUDJET: 50 000 000 SO'M):")
    print("-" * 65)
    for modda, summa in boshlangich_xarajatlar.items():
        ulush = (summa / jami_investitsiya) * 100
        print(f" - {modda:<32}: {format_som(summa):>16} ({ulush:4.1f}%)")
    print("-" * 65)
    print(f"   JAMI INVESTITSIYA:               {format_som(jami_investitsiya):>16} (100.0%)")

    # 2. Oylik operatsion xarajatlar
    oylik_xarajatlar = {
        "Do'kon ijarasi": 3_000_000,
        "Sotuvchi oyligi (+bonus)": 2_500_000,
        "Soliqlar (YTT va ijtimoiy)": 600_000,
        "Kommunal va tozalik": 400_000,
        "Marketing va SMM": 500_000,
        "Aloqa va logistika": 500_000,
    }

    jami_oylik_xarajat = sum(oylik_xarajatlar.values())

    print("\n2. DOIMIY OYLIK OPERATSION XARAJATLAR:")
    print("-" * 65)
    for xarajat, summa in oylik_xarajatlar.items():
        print(f" - {xarajat:<32}: {format_som(summa):>16}")
    print("-" * 65)
    print(f"   JAMI OYLIK XARAJAT:              {format_som(jami_oylik_xarajat):>16}")

    # 3. Daromad va foyda hisob-kitobi
    kunlik_xaridorlar = 11  # O'rtacha 8-15 kishi
    ortacha_chek = 130_000  # so'm
    ish_kunlari = 30

    oylik_tushum = kunlik_xaridorlar * ortacha_chek * ish_kunlari
    tannarx_ulushi = 0.65  # Mahsulot tannarxi ~65%
    sotilgan_tovar_tannarxi = oylik_tushum * tannarx_ulushi
    yalpi_foyda = oylik_tushum - sotilgan_tovar_tannarxi
    sof_foyda = yalpi_foyda - jami_oylik_xarajat

    rentabellik = (sof_foyda / oylik_tushum) * 100
    qoplanish_davri_oy = jami_investitsiya / sof_foyda

    print("\n3. OYLIK SAVDO VA FOYDA PROGNOZI:")
    print("-" * 65)
    print(f" - O'rtacha kunlik xaridorlar soni  : {kunlik_xaridorlar} nafar")
    print(f" - O'rtacha bitta xarid cheki       : {format_som(ortacha_chek)}")
    print(f" - Oylik yalpi tushum (savdo aylanma): {format_som(oylik_tushum)}")
    print(f" - Sotilgan tovarlar tannarxi (65%) : -{format_som(sotilgan_tovar_tannarxi)}")
    print(f" - Yalpi foyda (Marja ~35%)         : {format_som(yalpi_foyda)}")
    print(f" - Oylik doimiy xarajatlar          : -{format_som(jami_oylik_xarajat)}")
    print("=" * 65)
    print(f"   SOF OYLIK FOYDA                  :  {format_som(sof_foyda)}")
    print(f"   RENTABELLIK KO'RSATKICHI         :  {rentabellik:.1f}%")
    print(f"   LOYIHANING O'ZINI OQLASH MUDDATI :  {qoplanish_davri_oy:.1f} oy (taxminan 7 oy)")
    print("=" * 65)

    # 4. Yillik umumiy natija
    yillik_sof_foyda = sof_foyda * 12
    roi = (yillik_sof_foyda / jami_investitsiya) * 100

    print("\n4. YILLIK NAMOZ VA INVESTITSIYA QAYTIMI (ROI):")
    print("-" * 65)
    print(f" - 1 yillik sof foyda prognozi      : {format_som(yillik_sof_foyda)}")
    print(f" - Investitsiya qaytimi (ROI)       : {roi:.1f}%")
    print("=" * 65)

if __name__ == "__main__":
    main()
