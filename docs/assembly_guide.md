# Assembly Guide

## 1. PCB Fabrication
1. Gerber ज़िप JLCPCB पर अपलोड करें  
2. 2-layer, 1.6 mm, HASL, green soldermask सेट करें  
3. स्टेंसिल भी ऑर्डर करें (optional)

## 2. SMD Assembly
1. Stencil से paste प्रिंट करें  
2. Low-profile पार्ट्स पहले, ICs बाद में प्लेस करें  
3. Reflow profile:  
   - Preheat: 150 °C, 90 s  
   - Soak: 180 °C, 60 s  
   - Peak: 245 °C, 10 s  

## 3. Through-Hole & Connectors
- Wave soldering या हॉट-एयर से लागू करें  
- Visual inspection + continuity test करें  

## 4. Enclosure Integration
- PCB standoffs से माउंट करें  
- EMI Foil + conformal coating लगाएँ  
- Wire harness फिट करें  

## 5. Final Assembly
- Power-on test: BMS से सेल वोल्टेज वेरिफाई करें  
- UART console (RK3588/K210) चेक करें  
- ROS2 nodes लॉन्च करें  
