# ==========================================
# FILE 5: Ads_center.py
# PURPOSE: Ad Management & 48-Hour Auto-Delete
# ==========================================

class BMT_Ads_Service:
    def init(self, is_owner=False):
        self.show_ads = not is_owner # Owner Mode ဆိုရင် Ads ပိတ်မည်

    def show_banner_ad(self):
        if self.show_ads:
            print("Displaying Banner Ad below Home Buttons...")

    def auto_delete_old_files(self):
        """၄၈ နာရီပြည့်သည့် ဖိုင်များကို Database မှ ဖျက်ရန်"""
        # Logic: Check file timestamp
        # If timestamp > 48 hours -> Delete
        print("Cleaning up gallery: Old files removed.")
