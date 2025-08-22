from django.db import models


class Trip(models.Model):
    # Basic Info
    date = models.DateField()
    bilty_number = models.CharField(max_length=50)
    vehicle_number = models.CharField(max_length=50)

    # Driver Info
    driver_name = models.CharField(max_length=100)
    driver_mobile = models.CharField(max_length=20)

    # Trip Details
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    commodity = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=10, decimal_places=2)

    # Party Info
    adda_for_vehicle = models.CharField(max_length=100, blank=True)
    adda_for_load = models.CharField(max_length=100, blank=True)
    client_name = models.CharField(max_length=100)
    vendor = models.CharField(max_length=100, blank=True)

    # Financial
    amcs_rate = models.DecimalField(max_digits=10, decimal_places=2)
    vehicle_rate = models.DecimalField(max_digits=10, decimal_places=2)
    profit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    adda_commission = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    staff_commission = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    loading_unloading = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # Payment Info
    fare_type = models.CharField(max_length=20, choices=[
        ('Paid', 'Paid'),
        ('To Pay', 'To Pay'),
    ], default='To Pay')

    pod_status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Received', 'Received'),
    ], default='Pending')

    bill_status = models.CharField(max_length=20, choices=[
        ('Billed', 'Billed'),
        ('Unbilled', 'Unbilled'),
    ], default='Unbilled')

    payment_status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
        ('Partial', 'Partial'),
    ], default='Pending')

    payment_mode = models.CharField(max_length=20, choices=[
        ('Cash', 'Cash'),
        ('Cheque', 'Cheque'),
        ('Online', 'Online'),
    ], blank=True)

    cheque_details = models.CharField(max_length=100, blank=True)
    advance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    receivable = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payable = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Auto-calculate profit
        if self.amcs_rate and self.vehicle_rate:
            self.profit = self.amcs_rate - self.vehicle_rate

        # Auto-calculate balance
        if self.payable and self.advance:
            self.balance = self.payable - self.advance

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.bilty_number} - {self.vehicle_number}"