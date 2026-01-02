# ==========================================
# FILE 1: Styles.py
# PURPOSE: Premium Neon Aesthetics & UI/UX
# ==========================================

class BMT_Design_System:
    def init(self):
        # --- [Brand Colors] ---
        self.BLACK_BASE = "#000000"       # Deep Background
        self.NEON_CYAN = "#00F3FF"        # AI Chat Glow
        self.NEON_MAGENTA = "#BC13FE"     # Video Gen Glow
        self.GLASS_OVERLAY = "rgba(255, 255, 255, 0.1)" # Glassmorphism
        
        # --- [Tier Colors: F, S, G, D] ---
        self.COLOR_F = "#39FF14" # Neon Green
        self.COLOR_S = "#C0C0C0" # Silver
        self.COLOR_G = "#FFD700" # Gold
        self.COLOR_D = "#00BFFF" # Diamond Blue

    def get_button_style(self, type="chat"):
        """ခလုတ်များအတွက် Neon Glow Style ထုတ်ပေးရန်"""
        if type == "chat":
            return {
                "color": self.NEON_CYAN,
                "shadow": f"0 0 15px {self.NEON_CYAN}",
                "border": f"2px solid {self.NEON_CYAN}"
            }
        elif type == "video":
            return {
                "color": self.NEON_MAGENTA,
                "shadow": f"0 0 15px {self.NEON_MAGENTA}",
                "border": f"2px solid {self.NEON_MAGENTA}"
            }

    def get_haptic_feedback(self, tier):
        """Tier အလိုက် တုန်ခါမှု (Vibration) အဆင့် သတ်မှတ်ချက်"""
        vibe_map = {
            "F": "light",
            "S": "medium",
            "G": "heavy",
            "D": "ultra_vibrate"
        }
        return vibe_map.get(tier, "light")

# Logo Animation Logic
BMT_LOGO_GLOW = "breathing_animation 3s infinite"
