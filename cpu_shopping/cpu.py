msi_rtxa5000_price = 4199.35
gigabyte_aero_price = 4295.54
razer_blade15_price = 3696.99
asus_zephyrus_m16_price = 1849.79
hp_pavillion_price = 699.99
chromebook_price = 109.99

maxi=(float(max(msi_rtxa5000_price, gigabyte_aero_price, razer_blade15_price,asus_zephyrus_m16_price,hp_pavillion_price,chromebook_price)))
mini = (float(min(msi_rtxa5000_price, gigabyte_aero_price, razer_blade15_price,asus_zephyrus_m16_price,hp_pavillion_price,chromebook_price)))
roundi1 = print('price of msi is about',(round(msi_rtxa5000_price)))
roundi2= print('price of gigabyte is about',(round( gigabyte_aero_price)))
roundi3 = print('price of razer is about',(round(razer_blade15_price)))
roundi4 = print('price of asus is about',(round(asus_zephyrus_m16_price)))
roundi5 = print('price of hp is about',(round( hp_pavillion_price)))
roundi6 = print('price of chromebook is about',(round(chromebook_price)))
sumi=(round(msi_rtxa5000_price+gigabyte_aero_price+razer_blade15_price+asus_zephyrus_m16_price+hp_pavillion_price+chromebook_price))
sumiprint=print('if you were to buy all computers it would cost about',(round(msi_rtxa5000_price+gigabyte_aero_price+razer_blade15_price+asus_zephyrus_m16_price+hp_pavillion_price+chromebook_price)))
print('The highest cost of a laptop is',maxi)
print('The lowest cost of a laptop is', mini)
print("the average cost is about",(float(sumi//6)))