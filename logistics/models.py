from django.db import models


class Trip(models.Model):
    # Basic Info - REQUIRED
    date = models.DateField()  # Already required
    bilty_number = models.CharField(max_length=50)  # Already required
    vehicle_number = models.CharField(max_length=50)  # Already required

    # Driver Info
    driver_name = models.CharField(max_length=100)
    driver_mobile = models.CharField(max_length=20)

    # Trip Details - REQUIRED
    from_location = models.CharField(max_length=100)  # Already required
    to_location = models.CharField(max_length=100)  # Already required
    commodity = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=10, decimal_places=2)  # Already required

    # Party Info
    adda_for_vehicle = models.CharField(max_length=100, blank=True)
    adda_for_load = models.CharField(max_length=100, blank=True)
    client_name = models.CharField(max_length=100)
    vendor = models.CharField(max_length=100, blank=True)

    # Financial - ALL REQUIRED (CHANGE THESE)
    amcs_rate = models.DecimalField(max_digits=10, decimal_places=2)  # Remove blank=True, null=True if present
    vehicle_rate = models.DecimalField(max_digits=10, decimal_places=2)  # Remove blank=True, null=True
    profit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Keep as is (auto-calculated)
    adda_commission = models.DecimalField(max_digits=10, decimal_places=2)  # Remove default=0, make required
    staff_commission = models.DecimalField(max_digits=10, decimal_places=2)  # Remove default=0, make required
    loading_unloading = models.DecimalField(max_digits=10, decimal_places=2)  # Remove default=0, make required

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
    advance = models.DecimalField(max_digits=10, decimal_places=2)  # Remove default=0, make required
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    receivable = models.DecimalField(max_digits=10, decimal_places=2)  # Remove default=0, make required
    payable = models.DecimalField(max_digits=10, decimal_places=2)  # Remove default=0, make required

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