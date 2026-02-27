import os
import psycopg2
import openpyxl

DATABASE_URL = os.environ.get('DATABASE_URL')

conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()

cur.execute("""
    SELECT date, bilty_number, vehicle_number, driver_name, driver_mobile,
           from_location, to_location, commodity, weight,
           adda_for_vehicle, adda_for_load, client_name, vendor,
           amcs_rate, vehicle_rate, adda_commission, staff_commission,
           loading_unloading, receivable, payable, advance, profit,
           payment_status, bill_status, pod_status, payment_mode,
           fare_type, cheque_details
    FROM logistics_trip
    ORDER BY date DESC
""")

rows = cur.fetchall()

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Trips"

ws.append([
    'Date', 'Bilty #', 'Vehicle #', 'Driver Name', 'Driver Mobile',
    'From', 'To', 'Commodity', 'Weight (Tons)',
    'Adda for Vehicle', 'Adda for Load', 'Client Name', 'Vendor',
    'AMCS Rate', 'Vehicle Rate', 'Adda Commission', 'Staff Commission',
    'Loading/Unloading', 'Receivable', 'Payable', 'Advance', 'Profit',
    'Payment Status', 'Bill Status', 'POD Status', 'Payment Mode',
    'Fare Type', 'Cheque Details'
])

for row in rows:
    ws.append(list(row))

wb.save('trips_backup.xlsx')
print(f"Backup done: {len(rows)} trips exported")

cur.close()
conn.close()