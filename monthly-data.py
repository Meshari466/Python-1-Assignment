jan_sales = [1834., 1918.,  812., 1680., 2492., 2776., 2390., 2297.]
feb_sales = [2148., 1745., 2190., 1863., 2589., 2345., 2724., 2239., 2785., 1483., 2038., 2021.]
mar_sales = [1968., 1718., 1634., 2126., 1252., 2538., 2837., 1223., 2034., 1611., 2791.]
apr_sales = [2496., 2733.,  706., 2386., 3382., 1844., 1440., 2594., 1978., 2023., 2559., 1577.]
may_sales = [2832., 1681., 1954., 1801., 2294., 1732., 1638., 1949., 2676., 2329., 2370.]
jun_sales = [2335., 2538., 2186., 2186., 2622., 2564., 1269., 3124., 1286., 1689., 2627., 1345.]
jul_sales = [1651., 1957.,  853., 2229., 2990., 3148., 2917.,  952., 1583., 2447., 2491.]
aug_sales = [2520., 2540., 1756., 1562., 972., 2258., 1413., 1779., 2503., 2860.]
sep_sales = [1827., 2003., 1349., 1858., 1370., 1076., 2897., 2238.,   91., 1951., 2509., 2933.]
oct_sales = [1273., 3169., 1192., 2219., 2195., 3157., 2912., 2012.,  722.,  922.]
nov_sales = [1827., 2003., 1349., 1858., 1370., 1076., 2897., 2238.,   91., 1951., 2509., 2933.]
dec_sales = [2200., 2460., 1260., 3157., 2912., 2012.,  722.,  922.]

jan = sum(jan_sales)
feb = sum(feb_sales)
mar = sum(mar_sales)
apr = sum(apr_sales)
may = sum(may_sales)
jun = sum(jun_sales)
jul = sum(jul_sales)
aug = sum(aug_sales)
sep = sum(sep_sales)
oct = sum(oct_sales)
nov = sum(nov_sales)
dec = sum(dec_sales)
jan, feb, mar, apr, may, jun ,jul, aug, sep, oct ,nov, dec
annual_gross_revenue = jan + feb + mar + apr + may + jun + jul + aug + sep + oct + nov + dec
monthly_gross_revenue = 'jan:', jan, 'feb:', feb,'mar:', mar,'apr:', apr,'may:', may,'jun:', jun ,'jul:', jul,'aug:', aug,'sep:', sep,'oct:', oct , 'nov:', nov,'dec:',dec
quarterly_gross_revenue = 'Q1', jan + feb + mar, 'Q2', apr + may + jun, 'Q3', jul + aug + sep, 'Q4', oct + nov + dec
print(quarterly_gross_revenue)
print(annual_gross_revenue)
print(monthly_gross_revenue)
