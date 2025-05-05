# # import streamlit as st
# # import requests
# # import uuid
# # import os
# # import numpy as np
# # import joblib
# # from streamlit.components.v1 import html
# # from PIL import Image
# # import cv2
# # import numpy as np
# # from pyzbar.pyzbar import decode
# # import av
# # from streamlit_webrtc import webrtc_streamer, VideoTransformerBase

# # # Base configuration
# # BASE_URL = "http://127.0.0.1:5000"  # Update with your actual backend URL
# # MODEL_PATH = "models/fraud_detection_model.pkl"  # Ensure this path is correct

# # # Initialize session state
# # if 'qr_data' not in st.session_state:
# #     st.session_state.qr_data = None

# # # --- Page Configuration ---
# # st.set_page_config(
# #     page_title="UPI Fraud Detection",
# #     page_icon="💳",
# #     layout="wide",
# #     initial_sidebar_state="expanded"
# # )

# # # --- Navigation ---
# # st.sidebar.title("🔐 UPI Fraud Detection")
# # page = st.sidebar.radio("Navigate", [
# #      "🏠 Home", 
# #             "📁 File Malware Scan",
# #             "📷 QR Scan", 
# #             "💸 Fraud Detection",
# #            "🌐 Phishing Detection"
# # ])

# # # --- Style Functions ---
# # def set_custom_style():
# #     st.markdown("""
# #         <style>
# #             /* Main styles */
# #             body {
# #                 background-color: #f5f7fa;
# #                 font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
# #             }
# #             .main {
# #                 background-color: #ffffff;
# #                 padding: 2rem;
# #                 border-radius: 15px;
# #                 box-shadow: 0 4px 6px rgba(0,0,0,0.1);
# #                 margin-bottom: 2rem;
# #             }
            
# #             /* Card styles */
# #             .card {
# #                 background-color: #ffffff;
# #                 border-radius: 12px;
# #                 padding: 20px;
# #                 margin-bottom: 20px;
# #                 box-shadow: 0 2px 10px rgba(0,0,0,0.08);
# #                 transition: transform 0.3s, box-shadow 0.3s;
# #             }
# #             .card:hover {
# #                 transform: translateY(-5px);
# #                 box-shadow: 0 6px 15px rgba(0,0,0,0.1);
# #             }
# #             .card-title {
# #                 font-size: 1.1rem;
# #                 font-weight: 600;
# #                 margin-bottom: 10px;
# #                 color: #2c3e50;
# #             }
# #             .card-desc {
# #                 font-size: 0.9rem;
# #                 color: #7f8c8d;
# #             }
            
# #             /* Input styles */
# #             .stTextInput>div>div>input, 
# #             .stNumberInput>div>div>input,
# #             .stSelectbox>div>div>select {
# #                 border: 1px solid #dfe6e9;
# #                 border-radius: 8px;
# #                 padding: 10px;
# #             }
            
# #             /* Button styles */
# #             .stButton>button {
# #                 background-color: #3498db;
# #                 color: white;
# #                 border: none;
# #                 border-radius: 8px;
# #                 padding: 0.75rem 1.5rem;
# #                 font-size: 1rem;
# #                 transition: all 0.3s;
# #             }
# #             .stButton>button:hover {
# #                 background-color: #2980b9;
# #                 transform: translateY(-2px);
# #                 box-shadow: 0 4px 8px rgba(0,0,0,0.1);
# #             }
            
# #             /* Custom scrollbar */
# #             ::-webkit-scrollbar {
# #                 width: 8px;
# #             }
# #             ::-webkit-scrollbar-track {
# #                 background: #f1f1f1;
# #             }
# #             ::-webkit-scrollbar-thumb {
# #                 background: #bdc3c7;
# #                 border-radius: 4px;
# #             }
# #             ::-webkit-scrollbar-thumb:hover {
# #                 background: #95a5a6;
# #             }
            
# #             /* Animation classes */
# #             @keyframes shake {
# #                 0%, 100% { transform: translateX(0); }
# #                 10%, 30%, 50%, 70%, 90% { transform: translateX(-5px); }
# #                 20%, 40%, 60%, 80% { transform: translateX(5px); }
# #             }
# #             @keyframes pulse {
# #                 0% { transform: scale(1); }
# #                 50% { transform: scale(1.05); }
# #                 100% { transform: scale(1); }
# #             }
# #             .fraud-animation {
# #                 animation: shake 0.5s cubic-bezier(.36,.07,.19,.97) both;
# #             }
# #             .safe-animation {
# #                 animation: pulse 1s ease-in-out;
# #             }
            
# #             /* Smooth scrolling */
# #             html {
# #                 scroll-behavior: smooth;
# #             }
# #         </style>
# #     """, unsafe_allow_html=True)

# # def scan_result_card(status, score=None, details=None):
# #     style_map = {
# #         "Malicious": ("#e74c3c", "#ffebee"),
# #         "Suspicious": ("#f39c12", "#fff3e0"),
# #         "Clean": ("#2ecc71", "#e8f5e9")
# #     }
# #     border_color, bg_color = style_map.get(status, ("#95a5a6", "#f5f5f5"))

# #     st.markdown(f"""
# #         <div style='
# #             border-left: 5px solid {border_color};
# #             background-color: {bg_color};
# #             padding: 1.5rem;
# #             border-radius: 10px;
# #             margin: 1rem 0;
# #             transition: all 0.3s;
# #         '>
# #             <h4 style="margin-top: 0; color: {border_color};">🔍 Scan Result: {status}</h4>
# #             <p><b>Malware Probability Score:</b> {score if score is not None else "N/A"}</p>
# #             <p><b>Details:</b> {details if details else "No further explanation provided."}</p>
# #         </div>
# #     """, unsafe_allow_html=True)

# # # --- Home Page ---
# # if page == "🏠 Home":
# #     set_custom_style()
# #     st.title("🚀 Welcome to UPI Fraud Detection System")
# #     st.markdown("""
# #         <div style='text-align: center; margin-bottom: 2rem;'>
# #             <p style='font-size: 1.1rem; color: #7f8c8d;'>
# #                 Your comprehensive solution for secure digital transactions and fraud prevention
# #             </p>
# #         </div>
# #     """, unsafe_allow_html=True)

# #     col1, col2 = st.columns(2)

# #     with col1:
# #         st.markdown("""
# #             <div class='card'>
# #                 <div style='display: flex; justify-content: center; margin-bottom: 1rem;'>
# #                     <img src='https://cdn-icons-png.flaticon.com/512/1006/1006771.png' width='80'/>
# #                 </div>
# #                 <div class='card-title'>🔐 Register & Manage UPI IDs</div>
# #                 <div class='card-desc'>Securely register users and manage UPI IDs with our encrypted system</div>
# #             </div>
# #         """, unsafe_allow_html=True)

# #         st.markdown("""
# #             <div class='card'>
# #                 <div style='display: flex; justify-content: center; margin-bottom: 1rem;'>
# #                     <img src='https://cdn-icons-png.flaticon.com/512/2641/2641300.png' width='80'/>
# #                 </div>
# #                 <div class='card-title'>📁 File Threat Scanner</div>
# #                 <div class='card-desc'>Advanced scanning for PDF/DOCX files to detect malware and ransomware</div>
# #             </div>
# #         """, unsafe_allow_html=True)

# #     with col2:
# #         st.markdown("""
# #             <div class='card'>
# #                 <div style='display: flex; justify-content: center; margin-bottom: 1rem;'>
# #                     <img src='https://cdn-icons-png.flaticon.com/512/2920/2920222.png' width='80'/>
# #                 </div>
# #                 <div class='card-title'>🔍 UTR Verification</div>
# #                 <div class='card-desc'>Real-time verification of UTR IDs using machine learning algorithms</div>
# #             </div>
# #         """, unsafe_allow_html=True)

# #         st.markdown("""
# #             <div class='card'>
# #                 <div style='display: flex; justify-content: center; margin-bottom: 1rem;'>
# #                     <img src='https://cdn-icons-png.flaticon.com/512/5109/5109306.png' width='80'/>
# #                 </div>
# #                 <div class='card-title'>📷 QR Code Scanner</div>
# #                 <div class='card-desc'>Secure scanning of payment QR codes with tamper detection</div>
# #             </div>
# #         """, unsafe_allow_html=True)

# #     st.markdown("""
# #         <div style='margin-top: 2rem; padding: 1.5rem; background-color: #f8f9fa; border-radius: 12px;'>
# #             <h4 style='color: #2c3e50;'>Why Choose Our System?</h4>
# #             <p style='color: #7f8c8d;'>
# #                 With the exponential growth in digital payments, UPI fraud has become increasingly sophisticated. 
# #                 Our platform combines machine learning algorithms with real-time monitoring to provide comprehensive 
# #                 protection against various types of financial fraud. From account takeovers to phishing scams, 
# #                 we've got you covered.
# #             </p>
# #             <ul style='color: #7f8c8d;'>
# #                 <li>Real-time transaction monitoring</li>
# #                 <li>Advanced anomaly detection</li>
# #                 <li>Secure QR code validation</li>
# #                 <li>Document malware scanning</li>
# #                 <li>User-friendly dashboard</li>
# #             </ul>
# #         </div>
# #     """, unsafe_allow_html=True)

# # # --- Register User ---
# # elif page == "Register User":
# #     set_custom_style()
# #     st.title("📥 User Registration")
    
# #     with st.form("register_form"):
# #         name = st.text_input("Full Name", placeholder="Enter your full name", key="reg_name")
# #         phone = st.text_input("Phone Number", placeholder="Enter 10-digit mobile number", key="reg_phone")
# #         upi_id = st.text_input("UPI ID", placeholder="username@bank", key="reg_upi")
        
# #         if st.form_submit_button("Register User"):
# #             # Client-side validation
# #             if not all([name.strip(), phone.strip(), upi_id.strip()]):
# #                 st.warning("Please fill all fields")
# #             elif not phone.strip().isdigit() or len(phone.strip()) != 10:
# #                 st.warning("Phone must be 10 digits")
# #             elif "@" not in upi_id.strip():
# #                 st.warning("UPI ID must contain '@'")
# #             else:
# #                 try:
# #                     response = requests.post(
# #                         f"{BASE_URL}/register",
# #                         json={
# #                             "name": name.strip(),
# #                             "phone": phone.strip(),
# #                             "upi_id": upi_id.strip().lower()
# #                         },
# #                         timeout=5
# #                     )
                    
# #                     # Debugging output
# #                     st.write(f"Status Code: {response.status_code}")
# #                     st.write(f"Response Text: {response.text}")
                    
# #                     try:
# #                         response_json = response.json()
# #                     except ValueError:
# #                         st.error("Server returned invalid JSON. Is Flask running?")
# #                         pass
                        
# #                     if response.status_code == 201:
# #                         st.success("✅ Registration successful!")
# #                         st.json(response_json["user"])
# #                     else:
# #                         st.error(f"Error: {response_json.get('error', 'Unknown error')}")
                        
# #                 except requests.exceptions.RequestException as e:
# #                     st.error(f"Connection failed: {str(e)}")
# #                     st.error(f"Please ensure the Flask server is running at {BASE_URL}")
# # # --- Add UPI ---
# # elif page == "Add UPI":
# #     set_custom_style()
# #     st.title("➕ Add UPI ID")
    
# #     with st.form("add_upi_form"):
# #         phone = st.text_input("Registered Phone Number", placeholder="Enter registered phone number")
# #         new_upi = st.text_input("New UPI ID", placeholder="new_upi@bank")
        
# #         if st.form_submit_button("Add UPI ID"):
# #             if not all([phone, new_upi]):
# #                 st.warning("Please fill all fields")
# #             else:
# #                 try:
# #                     response = requests.post(
# #                         f"{BASE_URL}/add_upi", 
# #                         json={"phone": phone, "upi_id": new_upi},
# #                         timeout=5
# #                     )
                    
# #                     res = response.json()
# #                     if response.status_code == 200:
# #                         st.success(res.get("message", "UPI added successfully"))
# #                     elif response.status_code == 201:
# #                         st.info(res.get("message", "UPI updated successfully"))
# #                     elif response.status_code == 403:
# #                         st.error(res.get("error", "Operation not allowed"))
# #                     else:
# #                         st.warning(res.get("error", "Unknown error occurred"))
# #                 except requests.exceptions.RequestException as e:
# #                     st.error(f"Connection error: {str(e)}")

# # # --- Process Transaction ---
# # elif page == "Process Transaction":
# #     set_custom_style()
# #     st.title("💸 Process Transaction")
    
# #     with st.form("transaction_form"):
# #         col1, col2 = st.columns(2)
# #         with col1:
# #             sender_upi = st.text_input("Sender UPI ID", placeholder="your_upi@bank")
# #         with col2:
# #             receiver_upi = st.text_input("Receiver UPI ID", placeholder="recipient_upi@bank")
        
# #         amount = st.number_input("Amount (₹)", min_value=1, value=100, step=100)
# #         bank = st.text_input("Bank Name", placeholder="Your bank name")
        
# #         if st.form_submit_button("Process Transaction"):
# #             if not all([sender_upi, receiver_upi, amount, bank]):
# #                 st.warning("Please fill all fields")
# #             else:
# #                 try:
# #                     with st.spinner("Processing transaction..."):
# #                         response = requests.post(
# #                             f"{BASE_URL}/transaction", 
# #                             json={
# #                                 "sender_upi": sender_upi,
# #                                 "receiver_upi": receiver_upi,
# #                                 "amount": amount,
# #                                 "bank": bank
# #                             },
# #                             timeout=10
# #                         )
                        
# #                         if response.status_code in (200, 201):
# #                             result = response.json()
# #                             st.success("✅ Transaction processed successfully!")
# #                             with st.expander("View Transaction Details"):
# #                                 st.json(result)
# #                         else:
# #                             st.error(f"Transaction failed: {response.json().get('error', 'Unknown error')}")
# #                 except requests.exceptions.RequestException as e:
# #                     st.error(f"Connection error: {str(e)}")
# # # --- Verify UTR ---
# # elif page == "Verify UTR":
# #     set_custom_style()
# #     st.title("🔍 Verify UTR")
    
# #     with st.form("utr_form"):
# #         utr_id = st.text_input("Enter UTR ID", placeholder="Unique Transaction Reference ID")
        
# #         if st.form_submit_button("Verify UTR"):
# #             if not utr_id:
# #                 st.warning("Please enter a UTR ID")
# #             else:
# #                 try:
# #                     with st.spinner("Verifying UTR..."):
# #                         response = requests.get(
# #                             f"{BASE_URL}/check_utr", 
# #                             params={"utr_id": utr_id},
# #                             timeout=5
# #                         )
                        
# #                         if response.status_code == 200:
# #                             result = response.json()
# #                             transaction = result.get("transaction", {})
# #                             fraud_label = transaction.get("fraud_label", "Safe")

# #                             if fraud_label == "Fraud":
# #                                 st.error("""
# #                                 ## 🚨 Fraudulent Transaction Detected!
# #                                 *Recommendation:* Do not proceed with this transaction
# #                                 """)
# #                                 st.snow()
# #                             else:
# #                                 st.success("""
# #                                 ## ✅ Legitimate Transaction
# #                                 *Status:* This transaction appears to be safe
# #                                 """)
# #                                 st.balloons()
                            
# #                             with st.expander("Transaction Details"):
# #                                 st.json(transaction)

# #                         elif response.status_code == 404:
# #                             st.error("""
# #                             ## 🚨 Fake Transaction Detected!
# #                             *Warning:* UTR ID not found in database. Highly unsafe transaction!
# #                             """)
# #                             st.snow()
# #                         else:
# #                             st.error(f"Failed to verify UTR: {response.json().get('error', 'Unknown error')}")
                            
# #                 except requests.exceptions.RequestException as e:
# #                     st.error(f"Connection error: {str(e)}")
# # # --- File Malware Scan ---
# # elif page == "📁 File Malware Scan":
# #     set_custom_style()
# #     st.title("🛡️ File Malware Scanner")
    
# #     uploaded_file = st.file_uploader(
# #         "Upload a file for scanning", 
# #         type=["pdf", "docx", "doc"],
# #         help="Supported formats: PDF, DOCX"
# #     )
    
# #     if uploaded_file is not None:
# #         try:
# #             # Create uploads directory if not exists
# #             os.makedirs("uploads", exist_ok=True)
# #             file_id = str(uuid.uuid4())
# #             file_path = f"uploads/{file_id}_{uploaded_file.name}"
            
# #             # Save the uploaded file
# #             with open(file_path, "wb") as f:
# #                 f.write(uploaded_file.getbuffer())
            
# #             st.success(f"File '{uploaded_file.name}' uploaded successfully")
            
# #             # Perform the scan
# #             with st.spinner("Scanning file for malware..."):
# #                 with open(file_path, "rb") as f:
# #                     files = {"file": (uploaded_file.name, f)}
# #                     response = requests.post(
# #                         f"{BASE_URL}/scan", 
# #                         files=files,
# #                         timeout=15
# #                     )
                
# #                 if response.status_code == 200:
# #                     result = response.json()
# #                     status = result.get("status", "Unknown")
# #                     score = result.get("score", "N/A")
# #                     details = result.get("details", "No additional details available")
                    
# #                     scan_result_card(status, score, details)
                    
# #                     # Show additional file info
# #                     with st.expander("File Information"):
# #                         st.write(f"**Filename:** {uploaded_file.name}")
# #                         st.write(f"**Type:** {uploaded_file.type}")
# #                         st.write(f"**Size:** {uploaded_file.size / 1024:.2f} KB")
# #                 else:
# #                     st.error("Failed to scan file. Please try again.")
            
# #             # Clean up - remove the uploaded file
# #             try:
# #                 os.remove(file_path)
# #             except:
# #                 pass
                
# #         except Exception as e:
# #             st.error(f"An error occurred: {str(e)}")

# # # --- QR Scanner ---
# # elif page == "📷 QR Scan":
# #     set_custom_style()
# #     st.title("📷 QR Code Scanner")
    
# #     class QRScanner(VideoTransformerBase):
# #         def transform(self, frame):
# #             img = frame.to_ndarray(format="bgr24")
            
# #             # Convert to grayscale for QR detection
# #             gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# #             decoded = decode(gray)
            
# #             if decoded:
# #                 # Get the first QR code found
# #                 obj = decoded[0]
# #                 qr_data = obj.data.decode("utf-8")
                
# #                 # Draw bounding box around QR code
# #                 points = obj.polygon
# #                 if len(points) > 4:
# #                     hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
# #                     hull = list(map(tuple, np.squeeze(hull)))
# #                 else:
# #                     hull = points
                
# #                 # Draw the polygon
# #                 for j in range(len(hull)):
# #                     cv2.line(img, hull[j], hull[(j + 1) % len(hull)], (0, 255, 0), 3)
                
# #                 # Put text
# #                 cv2.putText(img, "QR DETECTED", (hull[0][0], hull[0][1] - 10),
# #                             cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                
# #                 # Store QR data in session state
# #                 if "qr_data" not in st.session_state or st.session_state.qr_data != qr_data:
# #                     st.session_state.qr_data = qr_data
            
# #             return img
    
# #     mode = st.radio("Select Scan Mode:", ["📤 Upload Image", "🎥 Live Camera"])
    
# #     if mode == "📤 Upload Image":
# #         uploaded_file = st.file_uploader(
# #             "Upload an image containing QR code", 
# #             type=["jpg", "jpeg", "png"]
# #         )
        
# #         if uploaded_file is not None:
# #             try:
# #                 image = Image.open(uploaded_file)
# #                 img_np = np.array(image.convert('RGB'))
                
# #                 # Detect QR codes
# #                 decoded = decode(img_np)
                
# #                 if decoded:
# #                     qr_data = decoded[0].data.decode("utf-8")
# #                     st.session_state.qr_data = qr_data
                    
# #                     # Draw on image
# #                     points = decoded[0].polygon
# #                     if len(points) > 4:
# #                         hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
# #                         hull = list(map(tuple, np.squeeze(hull)))
# #                     else:
# #                         hull = points
                    
# #                     for j in range(len(hull)):
# #                         cv2.line(img_np, hull[j], hull[(j + 1) % len(hull)], (0, 255, 0), 3)
                    
# #                     cv2.putText(img_np, "QR DETECTED", (hull[0][0], hull[0][1] - 10),
# #                                 cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                    
# #                     st.image(img_np, caption="Scanned Image", use_column_width=True)
# #                     st.success(f"QR Code Detected: {qr_data}")
# #                 else:
# #                     st.warning("No QR code found in the uploaded image")
# #                     st.image(img_np, caption="Uploaded Image", use_column_width=True)
# #             except Exception as e:
# #                 st.error(f"Error processing image: {str(e)}")
    
# #     elif mode == "🎥 Live Camera":
# #         st.info("Point your camera at a QR code to scan it automatically")
        
# #         # Start the webcam
# #         webrtc_ctx = webrtc_streamer(
# #             key="qr-scanner",
# #             video_transformer_factory=QRScanner,
# #             rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
# #             media_stream_constraints={"video": True, "audio": False},
# #         )
        
# #         if st.session_state.qr_data:
# #             st.success(f"Scanned QR Code: {st.session_state.qr_data}")
            
# #             if st.button("Clear Scan"):
# #                 st.session_state.qr_data = None
# #                 st.experimental_rerun()

# # # --- Fraud Detection ---
# # import streamlit as st
# # import pandas as pd
# # import numpy as np
# # from sklearn.model_selection import train_test_split
# # from sklearn.ensemble import RandomForestClassifier
# # from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
# # import matplotlib.pyplot as plt
# # import seaborn as sns
# # import joblib
# # import time
# # import re
# # if page == "💸 Fraud Detection":
# #     st.header("🔍 UPI Transaction Fraud Detection")

# #     # Define constants
# #     LOCATIONS = ['Mumbai', 'Delhi', 'Kolkata', 'Bangalore', 'Chennai',
# #                  'Hyderabad', 'Pune', 'Jaipur', 'Lucknow', 'Ahmedabad']
# #     STATES = ['Maharashtra', 'Delhi', 'West Bengal', 'Karnataka', 'Tamil Nadu',
# #               'Telangana', 'Uttar Pradesh', 'Gujarat', 'Rajasthan', 'Punjab']

# #     @st.cache_data
# #     def load_data():
# #         return pd.read_csv("upi_transaction_data.csv")

# #     def extract_upi_domain(upi_id):
# #         if pd.isna(upi_id) or upi_id == '':
# #             return 'unknown'
# #         patterns = [
# #             (r'.*@ok(sbi|hdfc|icici|axis|paytm)', 'legitimate_bank'),
# #             (r'.*@(oksbi|okhdfc|okicici|okaxis|okpaytm)', 'legitimate_bank'),
# #             (r'^\d+@upi$', 'legitimate_upi'),
# #         ]
# #         for pattern, label in patterns:
# #             if re.match(pattern, upi_id.lower()):
# #                 return label
# #         return 'suspicious_domain' if '@' in upi_id else 'unknown'

# #     def validate_phone(phone):
# #         phone_str = str(phone)
# #         return phone_str.isdigit() and len(phone_str) == 10 and phone_str[0] in '6789'

# #     def preprocess_data(df):
# #         df['Sender_Domain_Type'] = df["Sender's UPI ID"].apply(extract_upi_domain)
# #         df['Receiver_Domain_Type'] = df["Receiver's UPI ID"].apply(extract_upi_domain)

# #         domain_map = {'legitimate_bank': 0, 'legitimate_upi': 1, 'suspicious_domain': 2, 'unknown': 3}
# #         df['Sender_Domain_Encoded'] = df['Sender_Domain_Type'].map(domain_map)
# #         df['Receiver_Domain_Encoded'] = df['Receiver_Domain_Type'].map(domain_map)

# #         df['Phone_Valid'] = df["Sender's Phone Number"].apply(lambda x: int(validate_phone(x)))

# #         if 'Time of Transaction' in df.columns:
# #             df['Transaction_Date'] = pd.to_datetime(df['Time of Transaction'])
# #             df['Is_Night'] = ((df['Transaction_Date'].dt.hour >= 22) | 
# #                               (df['Transaction_Date'].dt.hour <= 6)).astype(int)

# #         df['Location_Encoded'] = df['Location'].apply(lambda x: LOCATIONS.index(x) if x in LOCATIONS else -1)
# #         df['State_Encoded'] = df['State'].apply(lambda x: STATES.index(x) if x in STATES else -1)

# #         bins = [0, 1000, 10000, 50000, 100000, float('inf')]
# #         df['Amount_Bin'] = pd.cut(df['Transaction Amount'], bins=bins, labels=False)

# #         return df

# #     # Load dataset and model
# #     df = load_data()
# #     df_processed = preprocess_data(df)

# #     try:
# #         model = joblib.load("enhanced_upi_fraud_model.pkl")
# #         model_loaded = True
# #     except FileNotFoundError:
# #         st.error("❌ Model not found. Please ensure the model file exists.")
# #         model_loaded = False

# #     if model_loaded:
# #         with st.form("fraud_form"):
# #             st.subheader("📄 Enter Transaction Details")

# #             col1, col2 = st.columns(2)
# #             with col1:
# #                 sender_name = st.text_input("Sender Name", "Pranjal Bhinge")
# #                 sender_upi = st.text_input("Sender UPI ID", "pranjalbhinge@oksbi")
# #                 phone = st.text_input("Sender Phone Number", "8431212363")
# #                 amount = st.number_input("Transaction Amount (₹)", min_value=1, value=548737)

# #             with col2:
# #                 receiver_upi = st.text_input("Receiver UPI ID", "brownpamela@example.com")
# #                 location = st.selectbox("Sender Location", LOCATIONS, index=2)
# #                 state = st.selectbox("Sender State", STATES, index=5)
# #                 trans_time = st.time_input("Transaction Time")

# #             if st.form_submit_button("Analyze Transaction"):
# #                 if amount > 60000:
# #                     st.error("❌ Transaction amount exceeds the maximum allowed limit of ₹60,000.")
# #                 elif not validate_phone(phone):
# #                     st.error("❌ Invalid phone number. Enter a 10-digit number starting with 6, 7, 8, or 9.")
# #                 else:
# #                     # Simulate one transaction
# #                     new_data = pd.DataFrame({
# #                         "Sender's UPI ID": [sender_upi],
# #                         "Sender's Phone Number": [phone],
# #                         "Transaction Amount": [amount],
# #                         "Receiver's UPI ID": [receiver_upi],
# #                         "Location": [location],
# #                         "State": [state],
# #                         "Time of Transaction": [f"2023-01-01 {trans_time}"],
# #                         "Fraudulent": [0]  # Dummy
# #                     })

# #                     processed = preprocess_data(new_data)

# #                     features = ['Transaction Amount', 'Sender_Domain_Encoded',
# #                                 'Receiver_Domain_Encoded', 'Location_Encoded',
# #                                 'State_Encoded', 'Phone_Valid', 'Amount_Bin']
# #                     if 'Is_Night' in processed.columns:
# #                         features.append('Is_Night')

# #                     probas = model.predict_proba(processed[features])[0]
# #                     prediction = model.predict(processed[features])[0]

# #                     st.subheader("🧾 Prediction Result")
# #                     if prediction:
# #                         st.error(f"⚠️ **Fraud Detected** — Confidence: {probas[1]*100:.2f}%")

# #                         st.markdown("#### Risk Factors Identified:")
# #                         risks = []
# #                         if extract_upi_domain(sender_upi) not in ['legitimate_bank', 'legitimate_upi']:
# #                             risks.append("❗ Unverified sender UPI domain")
# #                         if extract_upi_domain(receiver_upi) == 'suspicious_domain':
# #                             risks.append("❗ Suspicious receiver domain")
# #                         if not validate_phone(phone):
# #                             risks.append("❗ Invalid phone number format")
# #                         if amount > 50000:
# #                             risks.append("❗ High transaction amount")
# #                         if processed.get('Is_Night', [0])[0]:
# #                             risks.append("❗ Transaction during odd hours")

# #                         for r in risks:
# #                             st.write(r)
# #                     else:
# #                         st.success(f"✅ Legitimate Transaction — Confidence: {probas[0]*100:.2f}%")
# #                         st.markdown("#### Passed Checks:")
# #                         if extract_upi_domain(sender_upi) in ['legitimate_bank', 'legitimate_upi']:
# #                             st.write("✔️ Verified sender UPI domain")
# #                         if validate_phone(phone):
# #                             st.write("✔️ Valid Indian mobile number")
# #                         if amount <= 50000:
# #                             st.write("✔️ Reasonable transaction amount")


# # import streamlit as st
# # import google.generativeai as genai
# # import json
# # import os
# # from dotenv import load_dotenv


# # import streamlit as st
# # import json
# # import time
# # from streamlit_lottie import st_lottie
# # import requests
# # import random

# # # --- Phishing Detection Page ---
# # if page == "🌐 Phishing Detection":
# #     # Load environment variables
# #     load_dotenv()

# #     # Configure Gemini
# #     genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# #     # Specify the new model
# #     model_name = 'gemini-1.5-flash'
# #     try:
# #         model = genai.GenerativeModel(model_name)
# #         st.info(f"Using model: {model_name}")
# #     except Exception as e:
# #         st.error(f"Error loading model '{model_name}': {e}")
# #         st.stop()

# #     # Load Lottie animations
# #     def load_lottie_url(url):
# #         r = requests.get(url)
# #         if r.status_code != 200:
# #             return None
# #         return r.json()

# #     safe_animation = load_lottie_url("https://assets1.lottiefiles.com/packages/lf20_jbrw3hcz.json")
# #     danger_animation = load_lottie_url("https://assets1.lottiefiles.com/packages/lf20_6wutsrox.json")
# #     scanning_animation = load_lottie_url("https://assets1.lottiefiles.com/packages/lf20_pmvvft6i.json")

# #     # Website categories database (simplified example)
# #     WEBSITE_CATEGORIES = {
# #         "google.com": {"category": "Search Engine", "trust_score": 100},
# #         "facebook.com": {"category": "Social Media", "trust_score": 90},
# #         "amazon.com": {"category": "E-Commerce", "trust_score": 95},
# #         "sgbit.com": {"category": "Unknown", "trust_score": 10},
# #         "example.com": {"category": "Demo", "trust_score": 50}
# #     }

# #     def get_website_category(url):
# #         """Extract domain and match with known categories"""
# #         domain = url.split('//')[-1].split('/')[0].split('?')[0].lower()
# #         for site, data in WEBSITE_CATEGORIES.items():
# #             if site in domain:
# #                 return data
# #         return {"category": "Unknown", "trust_score": random.randint(10, 60)}

# #     def analyze_url(url):
# #         """Analyze URL for phishing and return enhanced output"""
# #         category_data = get_website_category(url)
        
# #         prompt = f"""Analyze this URL for phishing risk: {url}
# #         Respond with ONLY a valid JSON object containing:
# #         - is_phishing (boolean)
# #         - confidence (string: Low/Medium/High)
# #         - reasons (array of strings)
# #         - safe_to_visit (boolean)
# #         - website_type (string: Social Media/Banking/E-commerce/etc.)
# #         - risk_score (integer 0-100)
# #         - additional_advice (array of strings)

# #         Example output:
# #         {{
# #             "is_phishing": true,
# #             "confidence": "High",
# #             "reasons": [
# #                 "Misspelled domain name (sgbit vs sbi)",
# #                 "No SSL certificate",
# #                 "Suspicious login form"
# #             ],
# #             "safe_to_visit": false,
# #             "website_type": "Fake Banking",
# #             "risk_score": 87,
# #             "additional_advice": [
# #                 "Do not enter personal information",
# #                 "Check URL carefully",
# #                 "Report to your IT department"
# #             ]
# #         }}"""

# #         try:
# #             response = model.generate_content(prompt)
# #             json_str = response.text.strip().replace('```json', '').replace('```', '')
# #             result = json.loads(json_str)
# #             result.update(category_data)  # Add category data
# #             return result
# #         except Exception as e:
# #             return {"error": str(e), "category": "Unknown", "trust_score": 0}

# #     # Streamlit UI for Phishing Detection page
# #     st.title("🔒 Advanced Phishing Detector")
# #     st.markdown("### Protect yourself from malicious websites")
    
# #     with st.expander("ℹ️ How to use this tool"):
# #         st.write("""
# #         1. Enter any website URL in the box below
# #         2. Click "Analyze" to check for phishing risks
# #         3. View detailed security analysis
# #         4. Get safety recommendations
# #         """)

# #     url = st.text_input("Enter URL to analyze:", placeholder="https://example.com", key="phish_url")

# #     if st.button("🔍 Analyze", key="analyze_btn"):
# #         if url:
# #             with st.spinner("Scanning URL for threats..."):
# #                 # Show scanning animation
# #                 if scanning_animation:
# #                     st_lottie(scanning_animation, height=200, key="scanning")
                
# #                 result = analyze_url(url)
# #                 time.sleep(2)  # Simulate processing time

# #             st.subheader("🔍 Analysis Results")
            
# #             # Display animated result
# #             if "error" in result:
# #                 st.error(f"Error: {result['error']}")
# #             else:
# #                 # Result container with animation
# #                 with st.container():
# #                     cols = st.columns([1, 3])
# #                     with cols[0]:
# #                         if result['is_phishing']:
# #                             if danger_animation:
# #                                 st_lottie(danger_animation, height=150, key="danger")
# #                             st.error("DANGEROUS WEBSITE")
# #                         else:
# #                             if safe_animation:
# #                                 st_lottie(safe_animation, height=150, key="safe")
# #                             st.success("SAFE WEBSITE")
                    
# #                     with cols[1]:
# #                         st.metric("Risk Score", f"{result.get('risk_score', 0)}/100", 
# #                                  delta_color="inverse")
# #                         st.metric("Website Type", result.get('website_type', 'Unknown'))
# #                         st.metric("Category", result.get('category', 'Unknown'))
                
# #                 # Detailed results in expandable sections
# #                 with st.expander("📊 Detailed Analysis", expanded=True):
# #                     st.write(f"**Confidence Level:** {result['confidence']}")
                    
# #                     # Risk meter
# #                     risk_score = result.get('risk_score', 0)
# #                     st.progress(risk_score/100, text=f"Risk Meter: {risk_score}%")
                    
# #                     # Reasons section with icons
# #                     st.markdown("### 🚨 Potential Risks")
# #                     for reason in result["reasons"]:
# #                         st.write(f"⚠️ {reason}")
                    
# #                     # Advice section
# #                     st.markdown("### 🛡️ Safety Recommendations")
# #                     for advice in result.get("additional_advice", ["No specific recommendations"]):
# #                         st.write(f"✅ {advice}")
                
# #                 # Popup notification
# #                 if result['is_phishing']:
# #                     st.warning("""
# #                     ⚠️ WARNING: This website appears to be malicious!
# #                     Do not enter any personal information or credentials.
# #                     """, icon="⚠️")
# #                 else:
# #                     st.balloons()
# #                     st.success("""
# #                     ✔️ This website appears safe.
# #                     Always verify the URL before entering sensitive information.
# #                     """, icon="✅")
                
# #                 # Website comparison (if known)
# #                 if result.get('trust_score', 0) > 0:
# #                     st.markdown("### 📈 Trust Comparison")
# #                     trust_score = result['trust_score']
# #                     if trust_score > 80:
# #                         st.success(f"Trust Score: {trust_score}/100 (Highly Trusted)")
# #                     elif trust_score > 50:
# #                         st.warning(f"Trust Score: {trust_score}/100 (Moderately Trusted)")
# #                     else:
# #                         st.error(f"Trust Score: {trust_score}/100 (Low Trust)")
# #         else:
# #             st.warning("Please enter a URL to analyze")

# #     # Footer with tips
# #     st.markdown("---")
# #     st.markdown("""
# #     ### 🔍 Tips to Spot Phishing Sites:
# #     - Check for HTTPS and padlock icon
# #     - Look for misspelled domain names
# #     - Be wary of unsolicited login pages
# #     - Hover over links to see actual destination
# #     """)

# import streamlit as st
# import requests
# import uuid
# import os
# import numpy as np
# import joblib
# from streamlit.components.v1 import html
# from PIL import Image
# import cv2
# import numpy as np
# from pyzbar.pyzbar import decode
# import av
# from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
# import pandas as pd
# import re
# import time
# import random
# import google.generativeai as genai
# import json
# from dotenv import load_dotenv
# from streamlit_lottie import st_lottie

# # Base configuration
# BASE_URL = "http://127.0.0.1:5000"  # Update with your actual backend URL
# MODEL_PATH = "models/fraud_detection_model.pkl"  # Ensure this path is correct

# # Initialize session state
# if 'qr_data' not in st.session_state:
#     st.session_state.qr_data = None

# # --- Hacker Theme Configuration ---
# st.set_page_config(
#     page_title="UPI Fraud Detection System",
#     page_icon="💻",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # --- Hacker Style Functions ---
# def set_hacker_style():
#     st.markdown("""
#         <style>
#             /* Main styles */
                
            
#             .stRadio > div {
#                 background-color: #000000 !important;
#                 padding: 10px;
#                 border-radius: 5px;
#             }
#             .st-cc {
#                 color: black !important;
#                 font-weight: bold !important;
#             }
#             .st-cd {
#                 color: white !important;
#                 font-weight: bold !important;
#             }
#             .st-ae {
#                 color: white !important;
#             }
            
#             body {
#                 background-color: #0a0a0a;
#                 color: white;
#                 font-family: 'Courier New', monospace;
#             }
#             .main {
#                 background-color: #111111;
#                 padding: 2rem;
#                 border-radius: 5px;
#                 border: 1px solid #00ff00;
#                 margin-bottom: 2rem;
#             }
            
#             /* Text styles */
#             h1, h2, h3, h4, h5, h6, p, div, span {
#                 color: white !important;
#             }
            
#             /* Card styles */
#             .card {
#                 background-color: #111111;
#                 border-radius: 5px;
#                 padding: 20px;
#                 margin-bottom: 20px;
#                 border: 1px solid #00ff00;
#                 transition: all 0.3s;
#             }
#             .card:hover {
#                 box-shadow: 0 0 15px #00ff00;
#             }
#             .card-title {
#                 font-size: 1.1rem;
#                 font-weight: bold;
#                 margin-bottom: 10px;
#                 color: white !important;
#             }
#             .card-desc {
#                 font-size: 0.9rem;
#                 color: #cccccc !important;
#             }
            
#             /* Input styles */
#             .stTextInput>div>div>input, 
#             .stNumberInput>div>div>input,
#             .stSelectbox>div>div>select {
#                 background-color: #111111;
#                 color: white !important;
#                 border: 1px solid #00aa00;
#                 border-radius: 5px;
#                 padding: 10px;
#                 font-family: 'Courier New', monospace;
#             }
            
#             /* Button styles */
#             .stButton>button {
#                 background-color: #003300;
#                 color: #00ff00 !important;
#                 border: 1px solid #00aa00;
#                 border-radius: 5px;
#                 padding: 0.75rem 1.5rem;
#                 font-family: 'Courier New', monospace;
#                 transition: all 0.3s;
#             }
#             .stButton>button:hover {
#                 background-color: #005500;
#                 box-shadow: 0 0 10px #00ff00;
#             }
            
#             /* Terminal-like text */
#             .terminal {
#                 background-color: #000000;
#                 color: #00ff00;
#                 padding: 15px;
#                 border-radius: 5px;
#                 border: 1px solid #00aa00;
#                 font-family: 'Courier New', monospace;
#                 margin-bottom: 15px;
#             }
            
#             /* Custom scrollbar */
#             ::-webkit-scrollbar {
#                 width: 8px;
#             }
#             ::-webkit-scrollbar-track {
#                 background: #0a0a0a;
#             }
#             ::-webkit-scrollbar-thumb {
#                 background: #00aa00;
#                 border-radius: 4px;
#             }
#             ::-webkit-scrollbar-thumb:hover {
#                 background: #00ff00;
#             }
            
#             /* Animation classes */
#             @keyframes terminal-blink {
#                 0%, 100% { opacity: 1; }
#                 50% { opacity: 0; }
#             }
#             .terminal-cursor {
#                 animation: terminal-blink 1s step-end infinite;
#             }
            
#             /* Matrix rain effect */
#             .matrix-bg {
#                 position: fixed;
#                 top: 0;
#                 left: 0;
#                 width: 100%;
#                 height: 100%;
#                 z-index: -1;
#                 opacity: 0.1;
#             }
            
#             /* Logo styles */
#             .logo-container {
#                 display: flex;
#                 justify-content: center;
#                 margin-bottom: 1rem;
#             }
#             .logo {
#                 width: 80px;
#                 height: 80px;
#                 object-fit: contain;
#             }
#         </style>
#     """, unsafe_allow_html=True)
    
#     # Add Matrix rain effect
#     st.markdown("""
#         <canvas id="matrix" class="matrix-bg"></canvas>
#         <script>
#             const canvas = document.getElementById('matrix');
#             const ctx = canvas.getContext('2d');
            
#             canvas.width = window.innerWidth;
#             canvas.height = window.innerHeight;
            
#             const katakana = 'アァカサタナハマヤャラワガザダバパイィキシチニヒミリヰギジヂビピウゥクスツヌフムユュルグズブヅプエェケセテネヘメレヱゲゼデベペオォコソトノホモヨョロヲゴゾドボポヴッン';
#             const latin = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
#             const nums = '0123456789';
            
#             const alphabet = katakana + latin + nums;
            
#             const fontSize = 16;
#             const columns = canvas.width / fontSize;
            
#             const rainDrops = [];
            
#             for (let x = 0; x < columns; x++) {
#                 rainDrops[x] = 1;
#             }
            
#             const draw = () => {
#                 ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
#                 ctx.fillRect(0, 0, canvas.width, canvas.height);
                
#                 ctx.fillStyle = '#00ff00';
#                 ctx.font = fontSize + 'px monospace';
                
#                 for (let i = 0; i < rainDrops.length; i++) {
#                     const text = alphabet.charAt(Math.floor(Math.random() * alphabet.length));
#                     ctx.fillText(text, i * fontSize, rainDrops[i] * fontSize);
                    
#                     if (rainDrops[i] * fontSize > canvas.height && Math.random() > 0.975) {
#                         rainDrops[i] = 0;
#                     }
#                     rainDrops[i]++;
#                 }
#             };
            
#             setInterval(draw, 30);
#         </script>
#     """, unsafe_allow_html=True)

# def scan_result_card(status, score=None, details=None):
#     style_map = {
#         "Malicious": ("#ff5555", "#1a0000"),
#         "Suspicious": ("#ffaa00", "#1a0a00"),
#         "Clean": ("#00ff00", "#001a00")
#     }
#     text_color, bg_color = style_map.get(status, ("#00ff00", "#0a0a0a"))

#     st.markdown(f"""
#         <div style='
#             border-left: 5px solid {text_color};
#             background-color: {bg_color};
#             padding: 1.5rem;
#             border-radius: 5px;
#             margin: 1rem 0;
#             color: white;
#             font-family: 'Courier New', monospace;
#         '>
#             <h4 style="margin-top: 0; color: {text_color};">> SCAN_RESULT: {status}</h4>
#             <p style="color: white;">> MALWARE_PROBABILITY: {score if score is not None else "N/A"}</p>
#             <p style="color: white;">> DETAILS: {details if details else "No further data available."}</p>
#         </div>
#     """, unsafe_allow_html=True)

# # --- Logos ---
# LOGOS = {
#     "home": "https://cdn-icons-png.flaticon.com/512/1006/1006771.png",
#     "file_scan": "https://cdn-icons-png.flaticon.com/512/2641/2641300.png",
#     "qr_scan": "https://cdn-icons-png.flaticon.com/512/2920/2920222.png",
#     "fraud": "https://cdn-icons-png.flaticon.com/512/5109/5109306.png",
#     "phishing": "https://cdn-icons-png.flaticon.com/512/3064/3064155.png"
# }

# # --- Navigation ---
# st.sidebar.title("> UPI_FRAUD_DETECTION_SYSTEM")
# page = st.sidebar.radio("> NAVIGATION", [
#     "> HOME", 
#     "> FILE_SCAN",
#     "> QR_SCAN", 
#     "> FRAUD_DETECTION",
#     "> PHISHING_DETECTION"
# ])

# # --- Home Page ---
# if page == "> HOME":
#     set_hacker_style()
#     st.title("> UPI_FRAUD_DETECTION_SYSTEM v2.4.1")
    
#     # Header with logo
#     st.markdown("""
#         <div style="text-align: center; margin-bottom: 2rem;">
#             <img src="{logo}" class="logo">
#         </div>
#     """.format(logo=LOGOS["home"]), unsafe_allow_html=True)
    
#     st.markdown("""
#         <div class="terminal">
#             > Initializing system...<br>
#             > Loading modules...<br>
#             > Establishing secure connection...<br>
#             > System ready.<br><br>
#             > Welcome to UPI Fraud Detection System<br>
#             > Comprehensive security for digital transactions<br>
#             > Type 'help' for commands
#         </div>
#     """, unsafe_allow_html=True)

#     col1, col2 = st.columns(2)

#     with col1:
#         st.markdown("""
#             <div class='card'>
#                 <div class='logo-container'>
#                     <img src="{logo}" class="logo">
#                 </div>
#                 <div class='card-title'>[1] UPI_ID_MANAGEMENT</div>
#                 <div class='card-desc'>Secure registration and management of UPI IDs with encrypted protocols</div>
#             </div>
#         """.format(logo=LOGOS["fraud"]), unsafe_allow_html=True)

#         st.markdown("""
#             <div class='card'>
#                 <div class='logo-container'>
#                     <img src="{logo}" class="logo">
#                 </div>
#                 <div class='card-title'>[2] FILE_THREAT_ANALYSIS</div>
#                 <div class='card-desc'>Advanced scanning for PDF/DOCX files with heuristic analysis</div>
#             </div>
#         """.format(logo=LOGOS["file_scan"]), unsafe_allow_html=True)

#     with col2:
#         st.markdown("""
#             <div class='card'>
#                 <div class='logo-container'>
#                     <img src="{logo}" class="logo">
#                 </div>
#                 <div class='card-title'>[3] UTR_VERIFICATION</div>
#                 <div class='card-desc'>Real-time verification of UTR IDs using ML algorithms</div>
#             </div>
#         """.format(logo=LOGOS["fraud"]), unsafe_allow_html=True)

#         st.markdown("""
#             <div class='card'>
#                 <div class='logo-container'>
#                     <img src="{logo}" class="logo">
#                 </div>
#                 <div class='card-title'>[4] QR_CODE_ANALYSIS</div>
#                 <div class='card-desc'>Secure scanning of payment QR codes with tamper detection</div>
#             </div>
#         """.format(logo=LOGOS["qr_scan"]), unsafe_allow_html=True)

#     st.markdown("""
#         <div class="terminal" style='margin-top: 2rem;'>
#             > SYSTEM_FEATURES:<br>
#             > Real-time transaction monitoring<br>
#             > Advanced anomaly detection<br>
#             > Secure QR validation<br>
#             > Document malware scanning<br>
#             > Encrypted communication<br><br>
#             > Last system update: 2023-11-15<br>
#             > Security level: MAXIMUM<br>
#             > Connection: SECURE
#         </div>
#     """, unsafe_allow_html=True)

# # --- File Malware Scan ---
# elif page == "> FILE_SCAN":
#     set_hacker_style()
#     st.title("> FILE_THREAT_ANALYSIS")
    
#     # Header with logo
#     st.markdown("""
#         <div style="text-align: center; margin-bottom: 2rem;">
#             <img src="{logo}" class="logo">
#         </div>
#     """.format(logo=LOGOS["file_scan"]), unsafe_allow_html=True)
    
#     uploaded_file = st.file_uploader(
#         "> UPLOAD_FILE_FOR_ANALYSIS", 
#         type=["pdf", "docx", "doc"],
#         help="Supported formats: PDF, DOCX"
#     )
    
#     if uploaded_file is not None:
#         try:
#             # Create uploads directory if not exists
#             os.makedirs("uploads", exist_ok=True)
#             file_id = str(uuid.uuid4())
#             file_path = f"uploads/{file_id}_{uploaded_file.name}"
            
#             # Save the uploaded file
#             with open(file_path, "wb") as f:
#                 f.write(uploaded_file.getbuffer())
            
#             st.success(f"> FILE_UPLOAD_SUCCESS: '{uploaded_file.name}'")
            
#             # Perform the scan
#             with st.spinner("> ANALYZING_FILE_FOR_THREATS..."):
#                 with open(file_path, "rb") as f:
#                     files = {"file": (uploaded_file.name, f)}
#                     response = requests.post(
#                         f"{BASE_URL}/scan", 
#                         files=files,
#                         timeout=15
#                     )
                
#                 if response.status_code == 200:
#                     result = response.json()
#                     status = result.get("status", "UNKNOWN")
#                     score = result.get("score", "N/A")
#                     details = result.get("details", "No additional data available")
                    
#                     scan_result_card(status, score, details)
                    
#                     # Show additional file info
#                     with st.expander("> FILE_METADATA"):
#                         st.write(f"> FILENAME: {uploaded_file.name}")
#                         st.write(f"> TYPE: {uploaded_file.type}")
#                         st.write(f"> SIZE: {uploaded_file.size / 1024:.2f} KB")
#                 else:
#                     st.error("> ANALYSIS_FAILED: Please try again.")
            
#             # Clean up - remove the uploaded file
#             try:
#                 os.remove(file_path)
#             except:
#                 pass
                
#         except Exception as e:
#             st.error(f"> ERROR: {str(e)}")

# # --- QR Scanner ---
# elif page == "> QR_SCAN":
#     set_hacker_style()
#     st.title("> QR_CODE_ANALYSIS")
    
#     # Header with logo
#     st.markdown("""
#         <div style="text-align: center; margin-bottom: 2rem;">
#             <img src="{logo}" class="logo">
#         </div>
#     """.format(logo=LOGOS["qr_scan"]), unsafe_allow_html=True)
    
#     class QRScanner(VideoTransformerBase):
#         def transform(self, frame):
#             img = frame.to_ndarray(format="bgr24")
            
#             # Convert to grayscale for QR detection
#             gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#             decoded = decode(gray)
            
#             if decoded:
#                 # Get the first QR code found
#                 obj = decoded[0]
#                 qr_data = obj.data.decode("utf-8")
                
#                 # Draw bounding box around QR code
#                 points = obj.polygon
#                 if len(points) > 4:
#                     hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
#                     hull = list(map(tuple, np.squeeze(hull)))
#                 else:
#                     hull = points
                
#                 # Draw the polygon
#                 for j in range(len(hull)):
#                     cv2.line(img, hull[j], hull[(j + 1) % len(hull)], (0, 255, 0), 3)
                
#                 # Put text
#                 cv2.putText(img, "QR_DETECTED", (hull[0][0], hull[0][1] - 10),
#                             cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                
#                 # Store QR data in session state
#                 if "qr_data" not in st.session_state or st.session_state.qr_data != qr_data:
#                     st.session_state.qr_data = qr_data
            
#             return img
    
#     mode = st.radio("> SELECT_SCAN_MODE:", ["> UPLOAD_IMAGE", "> LIVE_CAMERA"])
    
#     if mode == "> UPLOAD_IMAGE":
#         uploaded_file = st.file_uploader(
#             "> UPLOAD_IMAGE_CONTAINING_QR", 
#             type=["jpg", "jpeg", "png"]
#         )
        
#         if uploaded_file is not None:
#             try:
#                 image = Image.open(uploaded_file)
#                 img_np = np.array(image.convert('RGB'))
                
#                 # Detect QR codes
#                 decoded = decode(img_np)
                
#                 if decoded:
#                     qr_data = decoded[0].data.decode("utf-8")
#                     st.session_state.qr_data = qr_data
                    
#                     # Draw on image
#                     points = decoded[0].polygon
#                     if len(points) > 4:
#                         hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
#                         hull = list(map(tuple, np.squeeze(hull)))
#                     else:
#                         hull = points
                    
#                     for j in range(len(hull)):
#                         cv2.line(img_np, hull[j], hull[(j + 1) % len(hull)], (0, 255, 0), 3)
                    
#                     cv2.putText(img_np, "QR_DETECTED", (hull[0][0], hull[0][1] - 10),
#                                 cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                    
#                     st.image(img_np, caption="SCANNED_IMAGE", use_column_width=True)
#                     st.success(f"> QR_CODE_DETECTED: {qr_data}")
#                 else:
#                     st.warning("> NO_QR_CODE_FOUND")
#                     st.image(img_np, caption="UPLOADED_IMAGE", use_column_width=True)
#             except Exception as e:
#                 st.error(f"> ERROR: {str(e)}")
    
#     elif mode == "> LIVE_CAMERA":
#         st.info("> POINT_CAMERA_AT_QR_CODE_TO_SCAN")
        
#         # Start the webcam
#         webrtc_ctx = webrtc_streamer(
#             key="qr-scanner",
#             video_transformer_factory=QRScanner,
#             rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
#             media_stream_constraints={"video": True, "audio": False},
#         )
        
#         if st.session_state.qr_data:
#             st.success(f"> SCANNED_DATA: {st.session_state.qr_data}")
            
#             if st.button("> CLEAR_SCAN"):
#                 st.session_state.qr_data = None
#                 st.experimental_rerun()

# # --- Fraud Detection ---
# elif page == "> FRAUD_DETECTION":
#     set_hacker_style()
#     st.title("> UPI_TRANSACTION_ANALYSIS")
    
#     # Header with logo
#     st.markdown("""
#         <div style="text-align: center; margin-bottom: 2rem;">
#             <img src="{logo}" class="logo">
#         </div>
#     """.format(logo=LOGOS["fraud"]), unsafe_allow_html=True)

#     # Define constants
#     LOCATIONS = ['Mumbai', 'Delhi', 'Kolkata', 'Bangalore', 'Chennai',
#                  'Hyderabad', 'Pune', 'Jaipur', 'Lucknow', 'Ahmedabad']
#     STATES = ['Maharashtra', 'Delhi', 'West Bengal', 'Karnataka', 'Tamil Nadu',
#               'Telangana', 'Uttar Pradesh', 'Gujarat', 'Rajasthan', 'Punjab']

#     @st.cache_data
#     def load_data():
#         return pd.read_csv("upi_transaction_data.csv")

#     def extract_upi_domain(upi_id):
#         if pd.isna(upi_id) or upi_id == '':
#             return 'unknown'
#         patterns = [
#             (r'.*@ok(sbi|hdfc|icici|axis|paytm)', 'legitimate_bank'),
#             (r'.*@(oksbi|okhdfc|okicici|okaxis|okpaytm)', 'legitimate_bank'),
#             (r'^\d+@upi$', 'legitimate_upi'),
#         ]
#         for pattern, label in patterns:
#             if re.match(pattern, upi_id.lower()):
#                 return label
#         return 'suspicious_domain' if '@' in upi_id else 'unknown'

#     def validate_phone(phone):
#         phone_str = str(phone)
#         return phone_str.isdigit() and len(phone_str) == 10 and phone_str[0] in '6789'

#     def preprocess_data(df):
#         df['Sender_Domain_Type'] = df["Sender's UPI ID"].apply(extract_upi_domain)
#         df['Receiver_Domain_Type'] = df["Receiver's UPI ID"].apply(extract_upi_domain)

#         domain_map = {'legitimate_bank': 0, 'legitimate_upi': 1, 'suspicious_domain': 2, 'unknown': 3}
#         df['Sender_Domain_Encoded'] = df['Sender_Domain_Type'].map(domain_map)
#         df['Receiver_Domain_Encoded'] = df['Receiver_Domain_Type'].map(domain_map)

#         df['Phone_Valid'] = df["Sender's Phone Number"].apply(lambda x: int(validate_phone(x)))

#         if 'Time of Transaction' in df.columns:
#             df['Transaction_Date'] = pd.to_datetime(df['Time of Transaction'])
#             df['Is_Night'] = ((df['Transaction_Date'].dt.hour >= 22) | 
#                               (df['Transaction_Date'].dt.hour <= 6)).astype(int)

#         df['Location_Encoded'] = df['Location'].apply(lambda x: LOCATIONS.index(x) if x in LOCATIONS else -1)
#         df['State_Encoded'] = df['State'].apply(lambda x: STATES.index(x) if x in STATES else -1)

#         bins = [0, 1000, 10000, 50000, 100000, float('inf')]
#         df['Amount_Bin'] = pd.cut(df['Transaction Amount'], bins=bins, labels=False)

#         return df

#     # Load dataset and model
#     df = load_data()
#     df_processed = preprocess_data(df)

#     try:
#         model = joblib.load("enhanced_upi_fraud_model.pkl")
#         model_loaded = True
#     except FileNotFoundError:
#         st.error("> ERROR: MODEL_NOT_FOUND")
#         model_loaded = False

#     if model_loaded:
#         with st.form("fraud_form"):
#             st.subheader("> ENTER_TRANSACTION_DETAILS")

#             col1, col2 = st.columns(2)
#             with col1:
#                 sender_name = st.text_input("> SENDER_NAME", "Pranjal Bhinge")
#                 sender_upi = st.text_input("> SENDER_UPI_ID", "pranjalbhinge@oksbi")
#                 phone = st.text_input("> SENDER_PHONE", "8431212363")
#                 amount = st.number_input("> AMOUNT(₹)", min_value=1, value=548737)

#             with col2:
#                 receiver_upi = st.text_input("> RECEIVER_UPI_ID", "brownpamela@example.com")
#                 location = st.selectbox("> LOCATION", LOCATIONS, index=2)
#                 state = st.selectbox("> STATE", STATES, index=5)
#                 trans_time = st.time_input("> TRANSACTION_TIME")

#             if st.form_submit_button("> ANALYZE_TRANSACTION"):
#                 if amount > 60000:
#                     st.error("> ERROR: AMOUNT_EXCEEDS_LIMIT")
#                 elif not validate_phone(phone):
#                     st.error("> ERROR: INVALID_PHONE_FORMAT")
#                 else:
#                     # Simulate one transaction
#                     new_data = pd.DataFrame({
#                         "Sender's UPI ID": [sender_upi],
#                         "Sender's Phone Number": [phone],
#                         "Transaction Amount": [amount],
#                         "Receiver's UPI ID": [receiver_upi],
#                         "Location": [location],
#                         "State": [state],
#                         "Time of Transaction": [f"2023-01-01 {trans_time}"],
#                         "Fraudulent": [0]  # Dummy
#                     })

#                     processed = preprocess_data(new_data)

#                     features = ['Transaction Amount', 'Sender_Domain_Encoded',
#                                 'Receiver_Domain_Encoded', 'Location_Encoded',
#                                 'State_Encoded', 'Phone_Valid', 'Amount_Bin']
#                     if 'Is_Night' in processed.columns:
#                         features.append('Is_Night')

#                     probas = model.predict_proba(processed[features])[0]
#                     prediction = model.predict(processed[features])[0]

#                     st.subheader("> ANALYSIS_RESULT")
#                     if prediction:
#                         st.error(f"> WARNING: FRAUD_DETECTED [CONFIDENCE: {probas[1]*100:.2f}%]")

#                         st.markdown("> RISK_FACTORS:")
#                         risks = []
#                         if extract_upi_domain(sender_upi) not in ['legitimate_bank', 'legitimate_upi']:
#                             risks.append("> UNVERIFIED_SENDER_UPI")
#                         if extract_upi_domain(receiver_upi) == 'suspicious_domain':
#                             risks.append("> SUSPICIOUS_RECEIVER_DOMAIN")
#                         if not validate_phone(phone):
#                             risks.append("> INVALID_PHONE_FORMAT")
#                         if amount > 50000:
#                             risks.append("> HIGH_TRANSACTION_AMOUNT")
#                         if processed.get('Is_Night', [0])[0]:
#                             risks.append("> ODD_HOURS_TRANSACTION")

#                         for r in risks:
#                             st.write(r)
#                     else:
#                         st.success(f"> CLEAN_TRANSACTION [CONFIDENCE: {probas[0]*100:.2f}%]")
#                         st.markdown("> PASSED_CHECKS:")
#                         if extract_upi_domain(sender_upi) in ['legitimate_bank', 'legitimate_upi']:
#                             st.write("> VERIFIED_SENDER_UPI")
#                         if validate_phone(phone):
#                             st.write("> VALID_PHONE_FORMAT")
#                         if amount <= 50000:
#                             st.write("> REASONABLE_AMOUNT")

# # --- Phishing Detection ---
# elif page == "> PHISHING_DETECTION":
#     set_hacker_style()
#     st.title("> PHISHING_DETECTION_SYSTEM")
    
#     # Header with logo
#     st.markdown("""
#         <div style="text-align: center; margin-bottom: 2rem;">
#             <img src="{logo}" class="logo">
#         </div>
#     """.format(logo=LOGOS["phishing"]), unsafe_allow_html=True)

#     # Load environment variables
#     load_dotenv()

#     # Configure Gemini
#     try:
#         genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
#     except Exception as e:
#         st.error(f"> ERROR: Failed to configure Gemini API - {str(e)}")
#         st.stop()

#     # Specify the new model
#     model_name = 'gemini-1.5-flash'
#     try:
#         model = genai.GenerativeModel(model_name)
#         st.info(f"> USING_MODEL: {model_name}")
#     except Exception as e:
#         st.error(f"> ERROR_LOADING_MODEL: {e}")
#         st.stop()

#     # Load Lottie animations with error handling
#     def load_lottie_url(url):
#         try:
#             r = requests.get(url, timeout=5)
#             if r.status_code == 200:
#                 return r.json()
#             return None
#         except:
#             return None

#     safe_animation = load_lottie_url("https://assets1.lottiefiles.com/packages/lf20_jbrw3hcz.json")
#     danger_animation = load_lottie_url("https://assets1.lottiefiles.com/packages/lf20_6wutsrox.json")
#     scanning_animation = load_lottie_url("https://assets1.lottiefiles.com/packages/lf20_pmvvft6i.json")

#     # Website categories database (simplified example)
#     WEBSITE_CATEGORIES = {
#         "google.com": {"category": "Search Engine", "trust_score": 100},
#         "facebook.com": {"category": "Social Media", "trust_score": 90},
#         "amazon.com": {"category": "E-Commerce", "trust_score": 95},
#         "sgbit.com": {"category": "Unknown", "trust_score": 10},
#         "example.com": {"category": "Demo", "trust_score": 50}
#     }

#     def get_website_category(url):
#         """Extract domain and match with known categories"""
#         if not url:
#             return {"category": "Unknown", "trust_score": 0}
            
#         try:
#             domain = url.split('//')[-1].split('/')[0].split('?')[0].lower()
#             for site, data in WEBSITE_CATEGORIES.items():
#                 if site in domain:
#                     return data
#             return {"category": "Unknown", "trust_score": random.randint(10, 60)}
#         except:
#             return {"category": "Unknown", "trust_score": 0}

#     def analyze_url(url):
#         """Analyze URL for phishing and return enhanced output"""
#         if not url:
#             return {"error": "No URL provided", "category": "Unknown", "trust_score": 0}
            
#         category_data = get_website_category(url)
        
#         prompt = f"""Analyze this URL for phishing risk: {url}
#         Respond with ONLY a valid JSON object containing:
#         - is_phishing (boolean)
#         - confidence (string: Low/Medium/High)
#         - reasons (array of strings)
#         - safe_to_visit (boolean)
#         - website_type (string: Social Media/Banking/E-commerce/etc.)
#         - risk_score (integer 0-100)
#         - additional_advice (array of strings)

#         Example output:
#         {{
#             "is_phishing": true,
#             "confidence": "High",
#             "reasons": [
#                 "Misspelled domain name (sgbit vs sbi)",
#                 "No SSL certificate",
#                 "Suspicious login form"
#             ],
#             "safe_to_visit": false,
#             "website_type": "Fake Banking",
#             "risk_score": 87,
#             "additional_advice": [
#                 "Do not enter personal information",
#                 "Check URL carefully",
#                 "Report to your IT department"
#             ]
#         }}"""

#         try:
#             response = model.generate_content(prompt)
#             json_str = response.text.strip().replace('```json', '').replace('```', '')
#             result = json.loads(json_str)
#             result.update(category_data)  # Add category data
#             return result
#         except Exception as e:
#             return {"error": str(e), "category": "Unknown", "trust_score": 0}

#     # Streamlit UI for Phishing Detection page
#     st.markdown("> PROTECT_YOURSELF_FROM_MALICIOUS_WEBSITES")
    
#     with st.expander("> HOW_TO_USE"):
#         st.write("""
#         1. Enter any website URL
#         2. Click 'Analyze' to check for threats
#         3. View security analysis
#         4. Get safety recommendations
#         """)

#     url = st.text_input("> ENTER_URL_TO_ANALYZE:", placeholder="https://example.com", key="phish_url")

#     if st.button("> ANALYZE", key="analyze_btn"):
#         if url:
#             with st.spinner("> SCANNING_URL..."):
#                 # Show scanning animation if available
#                 if scanning_animation:
#                     try:
#                         st_lottie(scanning_animation, height=200, key="scanning")
#                     except:
#                         pass
                
#                 result = analyze_url(url)
#                 time.sleep(1)  # Simulate processing time

#             st.subheader("> ANALYSIS_RESULTS")
            
#             # Display result
#             if "error" in result:
#                 st.error(f"> ERROR: {result['error']}")
#             else:
#                 # Result container with animation
#                 with st.container():
#                     cols = st.columns([1, 3])
#                     with cols[0]:
#                         if result['is_phishing']:
#                             if danger_animation:
#                                 try:
#                                     st_lottie(danger_animation, height=150, key="danger")
#                                 except:
#                                     pass
#                             st.error("> DANGEROUS_WEBSITE")
#                         else:
#                             if safe_animation:
#                                 try:
#                                     st_lottie(safe_animation, height=150, key="safe")
#                                 except:
#                                     pass
#                             st.success("> SAFE_WEBSITE")
                    
#                     with cols[1]:
#                         st.metric("> RISK_SCORE", f"{result.get('risk_score', 0)}/100", 
#                                  delta_color="inverse")
#                         st.metric("> WEBSITE_TYPE", result.get('website_type', 'UNKNOWN'))
#                         st.metric("> CATEGORY", result.get('category', 'UNKNOWN'))
                
#                 # Detailed results in expandable sections
#                 with st.expander("> DETAILED_ANALYSIS", expanded=True):
#                     st.write(f"> CONFIDENCE_LEVEL: {result['confidence']}")
                    
#                     # Risk meter
#                     risk_score = result.get('risk_score', 0)
#                     st.progress(risk_score/100, text=f"> RISK_METER: {risk_score}%")
                    
#                     # Reasons section
#                     st.markdown("> POTENTIAL_RISKS")
#                     if result.get("reasons"):
#                         for reason in result["reasons"]:
#                             st.write(f"> {reason}")
#                     else:
#                         st.write("> No specific risks identified")
                    
#                     # Advice section
#                     st.markdown("> SAFETY_RECOMMENDATIONS")
#                     if result.get("additional_advice"):
#                         for advice in result["additional_advice"]:
#                             st.write(f"> {advice}")
#                     else:
#                         st.write("> No specific recommendations")
                
#                 # Popup notification
#                 if result['is_phishing']:
#                     st.warning("""
#                     > WARNING: POTENTIAL_PHISHING_SITE
#                     > DO_NOT_ENTER_SENSITIVE_DATA
#                     """, icon="⚠️")
#                 else:
#                     st.balloons()
#                     st.success("""
#                     > CLEAN_WEBSITE
#                     > VERIFY_URL_BEFORE_PROCEEDING
#                     """, icon="✅")
                
#                 # Website comparison (if known)
#                 if result.get('trust_score', 0) > 0:
#                     st.markdown("> TRUST_COMPARISON")
#                     trust_score = result['trust_score']
#                     if trust_score > 80:
#                         st.success(f"> TRUST_SCORE: {trust_score}/100 (HIGH)")
#                     elif trust_score > 50:
#                         st.warning(f"> TRUST_SCORE: {trust_score}/100 (MEDIUM)")
#                     else:
#                         st.error(f"> TRUST_SCORE: {trust_score}/100 (LOW)")
#         else:
#             st.warning("> ERROR: NO_URL_PROVIDED")

#     # Footer with tips
#     st.markdown("---")
#     st.markdown("""
#     > SECURITY_TIPS:
#     - Check for HTTPS
#     - Verify domain spelling
#     - Beware of unsolicited login pages
#     - Hover over links before clicking
#     """)



import streamlit as st
import requests
import uuid
import os
import numpy as np
import joblib
from streamlit.components.v1 import html
from PIL import Image
import cv2
import numpy as np
from pyzbar.pyzbar import decode
import av
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import pandas as pd
import re
import time
import random
import google.generativeai as genai
import json
from dotenv import load_dotenv
from streamlit_lottie import st_lottie
from utils.analyzer import analyze_file
from datetime import datetime
# Base configuration
BASE_URL = "http://127.0.0.1:5000"  # Update with your actual backend URL
MODEL_PATH = "models/fraud_detection_model.pkl"  # Ensure this path is correct

# Initialize session state
if 'qr_data' not in st.session_state:
    st.session_state.qr_data = None
if 'current_page' not in st.session_state:
    st.session_state.current_page = "🏠 HOME"

# --- Custom Light Theme Configuration ---
st.set_page_config(
    page_title="UPI Fraud Detection System",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Light Theme with Pink/Blue Accents ---
def set_custom_style():
    st.markdown("""
        <style>
            /* Main styles */
            body {
                background-color: #f5f5f5;
                color: #333333;
                font-family: 'Courier New', monospace;
            }
            .main {
                background-color: #ffffff;
                padding: 2rem;
                border-radius: 10px;
                border: 1px solid #ff66b2;
                margin-bottom: 2rem;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            }
            
            /* Sidebar styles */
            .sidebar .sidebar-content {
                background-color: #e6f2ff !important;
                background-image: linear-gradient(to bottom, #e6f2ff, #cce6ff);
            }
            .sidebar .sidebar-content .block-container {
                background-color: transparent !important;
            }
            
            /* Text styles */
            h1, h2, h3, h4, h5, h6 {
                color: #333333 !important;
                border-bottom: 1px solid #ff66b2;
                padding-bottom: 0.3em;
            }
            
            /* Card styles */
            .card {
                background-color: #ffffff;
                border-radius: 10px;
                padding: 20px;
                margin-bottom: 20px;
                border: 1px solid #66b3ff;
                transition: all 0.3s;
                box-shadow: 0 2px 4px rgba(0,0,0,0.05);
                cursor: pointer;
            }
            .card:hover {
                box-shadow: 0 0 15px #66b3ff;
                transform: translateY(-5px);
            }
            .card-title {
                font-size: 1.1rem;
                font-weight: bold;
                margin-bottom: 10px;
                color: #333333 !important;
            }
            .card-desc {
                font-size: 0.9rem;
                color: #666666 !important;
            }
            
            /* Input styles */
            .stTextInput>div>div>input, 
            .stNumberInput>div>div>input,
            .stSelectbox>div>div>select {
                background-color: #ffffff;
                color: #333333 !important;
                border: 1px solid #66b3ff;
                border-radius: 5px;
                padding: 10px;
                font-family: 'Courier New', monospace;
            }
            
            /* Button styles */
            .stButton>button {
                background-color: #ff66b2;
                color: white !important;
                border: none;
                border-radius: 5px;
                padding: 0.75rem 1.5rem;
                font-family: 'Courier New', monospace;
                font-weight: bold;
                transition: all 0.3s;
            }
            .stButton>button:hover {
                background-color: #ff3385;
                box-shadow: 0 0 10px #ff66b2;
            }
            
            /* Terminal-like text */
            .terminal {
                background-color: #333333;
                color: #00ff00;
                padding: 15px;
                border-radius: 5px;
                border: 1px solid #ff66b2;
                font-family: 'Courier New', monospace;
                margin-bottom: 15px;
            }
            
            /* Custom scrollbar */
            ::-webkit-scrollbar {
                width: 8px;
            }
            ::-webkit-scrollbar-track {
                background: #f1f1f1;
            }
            ::-webkit-scrollbar-thumb {
                background: #ff66b2;
                border-radius: 4px;
            }
            ::-webkit-scrollbar-thumb:hover {
                background: #ff3385;
            }
            
            /* Animation classes */
            @keyframes terminal-blink {
                0%, 100% { opacity: 1; }
                50% { opacity: 0; }
            }
            .terminal-cursor {
                animation: terminal-blink 1s step-end infinite;
            }
            
            /* Floating bubbles animation */
            .bubbles {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                z-index: -1;
                opacity: 0.2;
                overflow: hidden;
            }
            .bubble {
                position: absolute;
                bottom: -100px;
                background: #66b3ff;
                border-radius: 50%;
                opacity: 0.5;
                animation: rise 10s infinite ease-in;
            }
            .bubble:nth-child(1) {
                width: 40px;
                height: 40px;
                left: 10%;
                animation-duration: 8s;
            }
            .bubble:nth-child(2) {
                width: 20px;
                height: 20px;
                left: 20%;
                animation-duration: 5s;
                animation-delay: 1s;
            }
            .bubble:nth-child(3) {
                width: 50px;
                height: 50px;
                left: 35%;
                animation-duration: 7s;
                animation-delay: 2s;
            }
            .bubble:nth-child(4) {
                width: 80px;
                height: 80px;
                left: 50%;
                animation-duration: 11s;
                animation-delay: 0s;
            }
            .bubble:nth-child(5) {
                width: 35px;
                height: 35px;
                left: 55%;
                animation-duration: 6s;
                animation-delay: 1s;
            }
            .bubble:nth-child(6) {
                width: 45px;
                height: 45px;
                left: 65%;
                animation-duration: 8s;
                animation-delay: 3s;
            }
            .bubble:nth-child(7) {
                width: 25px;
                height: 25px;
                left: 75%;
                animation-duration: 7s;
                animation-delay: 2s;
            }
            .bubble:nth-child(8) {
                width: 80px;
                height: 80px;
                left: 80%;
                animation-duration: 6s;
                animation-delay: 1s;
            }
            @keyframes rise {
                0% {
                    bottom: -100px;
                    transform: translateX(0);
                }
                50% {
                    transform: translate(100px);
                }
                100% {
                    bottom: 1080px;
                    transform: translateX(-200px);
                }
            }
            
            /* Logo styles */
            .logo-container {
                display: flex;
                justify-content: center;
                margin-bottom: 1rem;
            }
            .logo {
                width: 80px;
                height: 80px;
                object-fit: contain;
                filter: drop-shadow(0 0 5px rgba(0,0,0,0.2));
                transition: transform 0.3s;
            }
            .logo:hover {
                transform: scale(1.1);
            }
            
            /* Navigation icons */
            .nav-icon {
                margin-right: 10px;
                font-size: 1.2em;
                vertical-align: middle;
            }
            
            /* Pulse animation for important elements */
            @keyframes pulse {
                0% { transform: scale(1); }
                50% { transform: scale(1.05); }
                100% { transform: scale(1); }
            }
            .pulse {
                animation: pulse 2s infinite;
            }
        </style>
        
        <!-- Floating bubbles animation -->
        <div class="bubbles">
            <div class="bubble"></div>
            <div class="bubble"></div>
            <div class="bubble"></div>
            <div class="bubble"></div>
            <div class="bubble"></div>
            <div class="bubble"></div>
            <div class="bubble"></div>
            <div class="bubble"></div>
        </div>
    """, unsafe_allow_html=True)

def scan_result_card(status, score=None, details=None):
    style_map = {
        "Malicious": ("#ff3333", "#ffe6e6"),
        "Suspicious": ("#ff9933", "#fff2e6"),
        "Clean": ("#33cc33", "#e6ffe6")
    }
    text_color, bg_color = style_map.get(status, ("#66b3ff", "#e6f2ff"))

    st.markdown(f"""
        <div style='
            border-left: 5px solid {text_color};
            background-color: {bg_color};
            padding: 1.5rem;
            border-radius: 5px;
            margin: 1rem 0;
            color: #333333;
            font-family: 'Courier New', monospace;
        '>
            <h4 style="margin-top: 0; color: {text_color};">> SCAN_RESULT: {status}</h4>
            <p style="color: #333333;">> MALWARE_PROBABILITY: {score if score is not None else "N/A"}</p>
            <p style="color: #333333;">> DETAILS: {details if details else "No further data available."}</p>
        </div>
    """, unsafe_allow_html=True)

# --- Logos ---
LOGOS = {
    "home": "https://cdn-icons-png.flaticon.com/512/1006/1006771.png",
    "file_scan": "https://cdn-icons-png.flaticon.com/512/2641/2641300.png",
    "qr_scan": "https://cdn-icons-png.flaticon.com/512/2920/2920222.png",
    "fraud": "https://cdn-icons-png.flaticon.com/512/5109/5109306.png",
    "phishing": "https://cdn-icons-png.flaticon.com/512/3064/3064155.png"
}

# --- Navigation ---
def navigation():
    st.sidebar.title("UPI FRAUD DETECTION SYSTEM")
    page = st.sidebar.radio("NAVIGATION", [
        "🏠 HOME", 
        "📁 FILE SCAN",
        "📷 QR SCAN", 
        "💸 FRAUD DETECTION",
        "🎣 PHISHING DETECTION"
    ], index=["🏠 HOME", "📁 FILE SCAN", "📷 QR SCAN", "💸 FRAUD DETECTION", "🎣 PHISHING DETECTION"].index(st.session_state.current_page))
    
    st.session_state.current_page = page
    return page

page = navigation()

# --- Home Page ---
if page == "🏠 HOME":
    set_custom_style()
    st.title("UPI FRAUD DETECTION SYSTEM v2.4.1")
    
    # Header with logo
    st.markdown("""
        <div style="text-align: center; margin-bottom: 2rem;">
            <img src="{logo}" class="logo pulse">
        </div>
    """.format(logo=LOGOS["home"]), unsafe_allow_html=True)
    
    st.markdown("""
        <div class="terminal">
            > Initializing system...<br>
            > Loading modules...<br>
            > Establishing secure connection...<br>
            > System ready.<br><br>
            > Welcome to UPI Fraud Detection System<br>
            > Comprehensive security for digital transactions<br>
            > Type 'help' for commands
        </div>
    """, unsafe_allow_html=True)

    # Module showcase section with images
    st.subheader("MAIN SECURITY MODULES")
    
    # Create 4 columns for the module images
    img_col1, img_col2, img_col3, img_col4 = st.columns(4)
    
    with img_col1:
        st.image("images/phishing.png", 
                caption="Phishing Detection", width=130)
        st.markdown("""
        <div style="text-align: center; font-size: 0.9rem; margin-top: -1rem;">
            Detect fake UPI payment pages
        </div>
        """, unsafe_allow_html=True)
    
    with img_col2:
        st.image("images/malwarescan.webp", 
                caption="File Threat Analysis", width=120)
        st.markdown("""
        <div style="text-align: center; font-size: 0.9rem; margin-top: -1rem;">
            Scan malicious PDF/DOCX files
        </div>
        """, unsafe_allow_html=True)
    
    with img_col3:
        st.image("images/qr_scan.webp", 
                caption="QR Code Scanner", width=120)
        st.markdown("""
        <div style="text-align: center; font-size: 0.9rem; margin-top: -1rem;">
            Detect fraudulent QR codes
        </div>
        """, unsafe_allow_html=True)
    
    with img_col4:
        st.image("images/fraud.jpg", 
                caption="Fraud Detection", width=120)
        st.markdown("""
        <div style="text-align: center; font-size: 0.9rem; margin-top: -1rem;">
            Analyze suspicious transactions
        </div>
        """, unsafe_allow_html=True)

    # Interactive cards for navigation
    col1, col2 = st.columns(2)

    with col1:
        # File Threat Analysis Card
        if st.button("FILE THREAT ANALYSIS", key="file_scan_btn", use_container_width=True):
            st.session_state.current_page = "📁 FILE SCAN"
            st.experimental_rerun()
        st.markdown("""
            <div class='card' onclick="window.streamlit.navigateTo('?nav=📁 FILE SCAN')">
                <div class='logo-container'>
                    <img src="{logo}" class="logo">
                </div>
                <div class='card-title'>FILE THREAT ANALYSIS</div>
                <div class='card-desc'>Advanced scanning for PDF/DOCX files with heuristic analysis</div>
            </div>
        """.format(logo=LOGOS["file_scan"]), unsafe_allow_html=True)

        # Phishing Detection Card
        if st.button("PHISHING DETECTION", key="phishing_btn", use_container_width=True):
            st.session_state.current_page = "🎣 PHISHING DETECTION"
            st.experimental_rerun()
        st.markdown("""
            <div class='card' onclick="window.streamlit.navigateTo('?nav=🎣 PHISHING DETECTION')">
                <div class='logo-container'>
                    <img src="{logo}" class="logo">
                </div>
                <div class='card-title'>PHISHING DETECTION</div>
                <div class='card-desc'>Identify and block phishing attempts targeting UPI users</div>
            </div>
        """.format(logo=LOGOS["phishing"]), unsafe_allow_html=True)

    with col2:
        # QR Code Analysis Card
        if st.button("QR CODE ANALYSIS", key="qr_scan_btn", use_container_width=True):
            st.session_state.current_page = "📷 QR SCAN"
            st.experimental_rerun()
        st.markdown("""
            <div class='card' onclick="window.streamlit.navigateTo('?nav=📷 QR SCAN')">
                <div class='logo-container'>
                    <img src="{logo}" class="logo">
                </div>
                <div class='card-title'>QR CODE ANALYSIS</div>
                <div class='card-desc'>Secure scanning of payment QR codes with tamper detection</div>
            </div>
        """.format(logo=LOGOS["qr_scan"]), unsafe_allow_html=True)

        # Fraud Detection Card
        if st.button("FRAUD DETECTION", key="fraud_btn", use_container_width=True):
            st.session_state.current_page = "💸 FRAUD DETECTION"
            st.experimental_rerun()
        st.markdown("""
            <div class='card' onclick="window.streamlit.navigateTo('?nav=💸 FRAUD DETECTION')">
                <div class='logo-container'>
                    <img src="{logo}" class="logo">
                </div>
                <div class='card-title'>FRAUD DETECTION</div>
                <div class='card-desc'>Analyze transactions for suspicious patterns and fraud</div>
            </div>
        """.format(logo=LOGOS["fraud"]), unsafe_allow_html=True)

    # Add JavaScript for navigation
    st.markdown("""
        <script>
            // Function to handle card clicks
            function navigateTo(page) {
                window.location.href = window.location.pathname + '?nav=' + encodeURIComponent(page);
            }
        </script>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="terminal" style='margin-top: 2rem;'>
            > SYSTEM FEATURES:<br>
            > Real-time transaction monitoring<br>
            > Advanced anomaly detection<br>
            > Secure QR validation<br>
            > Document malware scanning<br>
            > Encrypted communication<br><br>
            > Last system update: 2023-11-15<br>
            > Security level: MAXIMUM<br>
            > Connection: SECURE
        </div>
    """, unsafe_allow_html=True)

# --- File Malware Scan ---
elif page == "📁 FILE SCAN":
    set_custom_style()
    st.title("🛡️ FILE THREAT ANALYSIS")
    
    # Header with logo
    st.markdown("""
        <div style="text-align: center; margin-bottom: 2rem;">
            <img src="{logo}" class="logo">
        </div>
    """.format(logo=LOGOS["file_scan"]), unsafe_allow_html=True)
    
    # File upload section
    uploaded_file = st.file_uploader(
        "UPLOAD FILE FOR ANALYSIS", 
        type=["pdf", "docx", "doc", "xls", "xlsx", "ppt", "pptx"],
        help="Supported formats: PDF, DOCX, DOC, XLS, XLSX, PPT, PPTX"
    )
    
    if uploaded_file is not None:
        try:
            # Create uploads directory if not exists
            os.makedirs("uploads", exist_ok=True)
            file_id = str(uuid.uuid4())
            file_path = f"uploads/{file_id}_{uploaded_file.name}"
            
            # Save the uploaded file
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            st.success(f"FILE UPLOAD SUCCESS: '{uploaded_file.name}'")
            
            # Display file info
            with st.expander("📄 FILE INFORMATION", expanded=True):
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("File Name", uploaded_file.name)
                with col2:
                    st.metric("File Size", f"{uploaded_file.size / 1024:.2f} KB")
                with col3:
                    st.metric("File Type", uploaded_file.type.split('/')[-1].upper())
            
            # Perform the scan
            with st.spinner("🔍 ANALYZING FILE FOR THREATS..."):
                # Call the enhanced analyzer directly
                analysis_result = analyze_file(file_path, uploaded_file.name)
                
                # Display results
                if analysis_result['status'] == 'malicious':
                    st.error(f"🚨 MALICIOUS FILE DETECTED: {uploaded_file.name}")
                elif analysis_result['status'] == 'suspicious':
                    st.warning(f"⚠️ SUSPICIOUS FILE DETECTED: {uploaded_file.name}")
                else:
                    st.success(f"✅ FILE APPEARS SAFE: {uploaded_file.name}")
                
                # Threat score visualization
                st.subheader("THREAT ASSESSMENT")
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.metric("Threat Score", f"{analysis_result['threat_score'] * 100:.0f}%")
                with col2:
                    st.progress(float(analysis_result['threat_score']))
                
                # Detailed analysis
                with st.expander("🔬 DETAILED ANALYSIS RESULTS", expanded=True):
                    st.write(f"**Detection Method:** {analysis_result['method'].upper()}")
                    st.write(f"**Details:** {analysis_result['details']}")
                    
                    # Technical indicators
                    st.subheader("TECHNICAL INDICATORS")
                    st.write(f"**Entropy Level:** {analysis_result.get('entropy', 0):.4f}")
                    st.write(f"**SHA256 Hash:** `{analysis_result.get('hash', '')}`")
                    
                    # Suspicious patterns if found
                    if analysis_result.get('suspicious_patterns'):
                        st.subheader("SUSPICIOUS PATTERNS DETECTED")
                        for pattern in analysis_result['suspicious_patterns']:
                            st.write(f"🔍 **Pattern:** `{pattern['pattern']}`")
                            st.write(f"   - Count: {pattern['count']}")
                            if pattern.get('sample'):
                                st.code(pattern['sample'][:100] + ("..." if len(pattern['sample']) > 100 else ""))
            
            # Clean up - remove the uploaded file
            try:
                os.remove(file_path)
            except:
                pass
                
            # Add to scan history
            if 'scan_history' not in st.session_state:
                st.session_state.scan_history = []
            
            analysis_result['filename'] = uploaded_file.name
            analysis_result['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            st.session_state.scan_history.insert(0, analysis_result)
            
            # Display scan history
            st.subheader("📜 SCAN HISTORY")
            if st.session_state.scan_history:
                history_df = pd.DataFrame(st.session_state.scan_history)
                
                # Format the display
                history_display = history_df[['timestamp', 'filename', 'status', 'threat_score']].copy()
                history_display['threat_score'] = history_display['threat_score'].apply(lambda x: f"{x * 100:.0f}%")
                history_display['status'] = history_display['status'].apply(
                    lambda x: f"🟢 SAFE" if x == 'safe' else f"🟡 SUSPICIOUS" if x == 'suspicious' else f"🔴 MALICIOUS"
                )
                
                st.dataframe(
                    history_display,
                    column_config={
                        "timestamp": "Scan Time",
                        "filename": "File Name",
                        "status": "Status",
                        "threat_score": "Threat Score"
                    },
                    use_container_width=True,
                    hide_index=True
                )
            else:
                st.info("No scan history available")
                
        except Exception as e:
            st.error(f"❌ ERROR DURING ANALYSIS: {str(e)}")
            st.exception(e)
# --- QR Scanner ---
elif page == "📷 QR SCAN":
    set_custom_style()
    st.title("📷 QR CODE ANALYSIS")
    
    # Header with logo
    st.markdown("""
        <div style="text-align: center; margin-bottom: 2rem;">
            <img src="{logo}" class="logo">
        </div>
    """.format(logo=LOGOS["qr_scan"]), unsafe_allow_html=True)
    
    # Fraud detection logic
    def check_if_fraud(url):
        suspicious_keywords = ["login", "verify", "update", "bank", "secure", "account", "paypal", "password"]
        for word in suspicious_keywords:
            if re.search(word, url, re.IGNORECASE):
                return "Fraud"
        return "Safe"
    
    class QRScanner(VideoTransformerBase):
        def __init__(self):
            self.detected_qr = None
            self.frame = None
            
        def transform(self, frame):
            img = frame.to_ndarray(format="bgr24")
            self.frame = img.copy()  # Store the current frame
            
            # Convert to grayscale for QR detection
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            decoded = decode(gray)
            
            if decoded:
                # Get the first QR code found
                obj = decoded[0]
                qr_data = obj.data.decode("utf-8")
                self.detected_qr = qr_data
                
                # Draw bounding box around QR code
                points = obj.polygon
                if len(points) > 4:
                    hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                    hull = list(map(tuple, np.squeeze(hull)))
                else:
                    hull = points
                
                # Draw the polygon
                for j in range(len(hull)):
                    cv2.line(img, hull[j], hull[(j + 1) % len(hull)], (0, 255, 0), 3)
                
                # Put text
                cv2.putText(img, "QR DETECTED", (hull[0][0], hull[0][1] - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            
            return img
    
    mode = st.radio("SELECT SCAN MODE:", ["📤 Upload Image", "🎥 Live Camera"])
    
    if mode == "📤 Upload Image":
        uploaded_file = st.file_uploader(
            "UPLOAD IMAGE CONTAINING QR", 
            type=["jpg", "jpeg", "png"]
        )
        
        if uploaded_file is not None:
            try:
                image = Image.open(uploaded_file)
                img_np = np.array(image.convert('RGB'))
                
                # Detect QR codes
                decoded = decode(img_np)
                
                if decoded:
                    qr_data = decoded[0].data.decode("utf-8")
                    st.session_state.qr_data = qr_data
                    
                    # Draw on image
                    points = decoded[0].polygon
                    if len(points) > 4:
                        hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                        hull = list(map(tuple, np.squeeze(hull)))
                    else:
                        hull = points
                    
                    for j in range(len(hull)):
                        cv2.line(img_np, hull[j], hull[(j + 1) % len(hull)], (0, 255, 0), 3)
                    
                    cv2.putText(img_np, "QR DETECTED", (hull[0][0], hull[0][1] - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                    
                    st.image(img_np, caption="SCANNED IMAGE", use_column_width=True)

                    # Check if link is safe or fraud
                    status = check_if_fraud(qr_data)
                    if status == "Fraud":
                        st.error(f"⚠️ Warning: Fraudulent QR Code!\n\nLink: {qr_data}")
                    else:
                        st.success(f"✅ Safe QR Code Detected!\n\nLink: {qr_data}")
                    
                else:
                    st.warning("NO QR CODE FOUND")
                    st.image(img_np, caption="UPLOADED IMAGE", use_column_width=True)
            except Exception as e:
                st.error(f"ERROR: {str(e)}")
    
    elif mode == "🎥 Live Camera":
        st.info("POINT CAMERA AT QR CODE TO SCAN")
        
        # Initialize session state variables if they don't exist
        if 'qr_data' not in st.session_state:
            st.session_state.qr_data = None
        if 'qr_status' not in st.session_state:
            st.session_state.qr_status = None
        if 'scanned_image' not in st.session_state:
            st.session_state.scanned_image = None
        
        # Start the webcam
        webrtc_ctx = webrtc_streamer(
            key="qr-scanner",
            video_transformer_factory=QRScanner,
            rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
            media_stream_constraints={"video": True, "audio": False},
        )
        
        # Add scan button
        scan_button = st.button("Scan and Check")
        
        # Display area for QR code results
        result_placeholder = st.empty()
        image_placeholder = st.empty()
        
        # Check if we have a transformer and the scan button was clicked
        if webrtc_ctx.video_transformer and scan_button:
            scanner = webrtc_ctx.video_transformer
            if scanner.detected_qr:
                # Store the QR data and status
                st.session_state.qr_data = scanner.detected_qr
                st.session_state.qr_status = check_if_fraud(scanner.detected_qr)
                
                # Store the captured frame
                if scanner.frame is not None:
                    st.session_state.scanned_image = scanner.frame
            
        # Display results if we have them
        if st.session_state.qr_data:
            # Show the captured image with QR code highlighted
            if st.session_state.scanned_image is not None:
                image_placeholder.image(st.session_state.scanned_image, 
                                      caption="Captured QR Code", 
                                      channels="BGR",
                                      use_column_width=True)
            
            # Show the safety status
            if st.session_state.qr_status == "Fraud":
                result_placeholder.error(f"⚠️ Warning: Fraudulent QR Code!\n\nLink: {st.session_state.qr_data}")
            else:
                result_placeholder.success(f"✅ Safe QR Code Detected!\n\nLink: {st.session_state.qr_data}")
            
            if st.button("Clear Scan"):
                st.session_state.qr_data = None
                st.session_state.qr_status = None
                st.session_state.scanned_image = None
                result_placeholder.empty()
                image_placeholder.empty()
                st.experimental_rerun()

# --- Fraud Detection ---
elif page == "💸 FRAUD DETECTION":
    set_custom_style()
    st.title("💸 UPI TRANSACTION ANALYSIS")
    
    # Header with logo
    st.markdown("""
        <div style="text-align: center; margin-bottom: 2rem;">
            <img src="{logo}" class="logo">
        </div>
    """.format(logo=LOGOS["fraud"]), unsafe_allow_html=True)

    # Define constants
    LOCATIONS = ['Mumbai', 'Delhi', 'Kolkata', 'Bangalore', 'Chennai',
                 'Hyderabad', 'Pune', 'Jaipur', 'Lucknow', 'Ahmedabad']
    STATES = ['Maharashtra', 'Delhi', 'West Bengal', 'Karnataka', 'Tamil Nadu',
              'Telangana', 'Uttar Pradesh', 'Gujarat', 'Rajasthan', 'Punjab']

    @st.cache_data
    def load_data():
        return pd.read_csv("upi_transaction_data.csv")

    def extract_upi_domain(upi_id):
        if pd.isna(upi_id) or upi_id == '':
            return 'unknown'
        patterns = [
            (r'.*@ok(sbi|hdfc|icici|axis|paytm)', 'legitimate_bank'),
            (r'.*@(oksbi|okhdfc|okicici|okaxis|okpaytm)', 'legitimate_bank'),
            (r'^\d+@upi$', 'legitimate_upi'),
        ]
        for pattern, label in patterns:
            if re.match(pattern, upi_id.lower()):
                return label
        return 'suspicious_domain' if '@' in upi_id else 'unknown'

    def validate_phone(phone):
        phone_str = str(phone)
        return phone_str.isdigit() and len(phone_str) == 10 and phone_str[0] in '6789'

    def preprocess_data(df):
        df['Sender_Domain_Type'] = df["Sender's UPI ID"].apply(extract_upi_domain)
        df['Receiver_Domain_Type'] = df["Receiver's UPI ID"].apply(extract_upi_domain)

        domain_map = {'legitimate_bank': 0, 'legitimate_upi': 1, 'suspicious_domain': 2, 'unknown': 3}
        df['Sender_Domain_Encoded'] = df['Sender_Domain_Type'].map(domain_map)
        df['Receiver_Domain_Encoded'] = df['Receiver_Domain_Type'].map(domain_map)

        df['Phone_Valid'] = df["Sender's Phone Number"].apply(lambda x: int(validate_phone(x)))

        if 'Time of Transaction' in df.columns:
            df['Transaction_Date'] = pd.to_datetime(df['Time of Transaction'])
            df['Is_Night'] = ((df['Transaction_Date'].dt.hour >= 22) | 
                              (df['Transaction_Date'].dt.hour <= 6)).astype(int)

        df['Location_Encoded'] = df['Location'].apply(lambda x: LOCATIONS.index(x) if x in LOCATIONS else -1)
        df['State_Encoded'] = df['State'].apply(lambda x: STATES.index(x) if x in STATES else -1)

        bins = [0, 1000, 10000, 50000, 100000, float('inf')]
        df['Amount_Bin'] = pd.cut(df['Transaction Amount'], bins=bins, labels=False)

        return df

    # Load dataset and model
    df = load_data()
    df_processed = preprocess_data(df)

    try:
        model = joblib.load("enhanced_upi_fraud_model.pkl")
        model_loaded = True
    except FileNotFoundError:
        st.error("ERROR: MODEL NOT FOUND")
        model_loaded = False

    if model_loaded:
        with st.form("fraud_form"):
            st.subheader("ENTER TRANSACTION DETAILS")

            col1, col2 = st.columns(2)
            with col1:
                sender_name = st.text_input("SENDER NAME", "Pranjal Bhinge")
                sender_upi = st.text_input("SENDER UPI ID", "pranjalbhinge@oksbi")
                phone = st.text_input("SENDER PHONE", "8431212363")
                amount = st.number_input("AMOUNT(₹)", min_value=1, value=548737)

            with col2:
                receiver_upi = st.text_input("RECEIVER UPI ID", "brownpamela@example.com")
                location = st.selectbox("LOCATION", LOCATIONS, index=2)
                state = st.selectbox("STATE", STATES, index=5)
                trans_time = st.time_input("TRANSACTION TIME")

            if st.form_submit_button("ANALYZE TRANSACTION"):
                if amount > 60000:
                    st.error("ERROR: AMOUNT EXCEEDS LIMIT")
                elif not validate_phone(phone):
                    st.error("ERROR: INVALID PHONE FORMAT")
                else:
                    # Simulate one transaction
                    new_data = pd.DataFrame({
                        "Sender's UPI ID": [sender_upi],
                        "Sender's Phone Number": [phone],
                        "Transaction Amount": [amount],
                        "Receiver's UPI ID": [receiver_upi],
                        "Location": [location],
                        "State": [state],
                        "Time of Transaction": [f"2023-01-01 {trans_time}"],
                        "Fraudulent": [0]  # Dummy
                    })

                    processed = preprocess_data(new_data)

                    features = ['Transaction Amount', 'Sender_Domain_Encoded',
                                'Receiver_Domain_Encoded', 'Location_Encoded',
                                'State_Encoded', 'Phone_Valid', 'Amount_Bin']
                    if 'Is_Night' in processed.columns:
                        features.append('Is_Night')

                    probas = model.predict_proba(processed[features])[0]
                    prediction = model.predict(processed[features])[0]

                    st.subheader("ANALYSIS RESULT")
                    if prediction:
                        st.error(f"WARNING: FRAUD DETECTED [CONFIDENCE: {probas[1]*100:.2f}%]")

                        st.markdown("RISK FACTORS:")
                        risks = []
                        if extract_upi_domain(sender_upi) not in ['legitimate_bank', 'legitimate_upi']:
                            risks.append("UNVERIFIED SENDER UPI")
                        if extract_upi_domain(receiver_upi) == 'suspicious_domain':
                            risks.append("SUSPICIOUS RECEIVER DOMAIN")
                        if not validate_phone(phone):
                            risks.append("INVALID PHONE FORMAT")
                        if amount > 50000:
                            risks.append("HIGH TRANSACTION AMOUNT")
                        if processed.get('Is_Night', [0])[0]:
                            risks.append("ODD HOURS TRANSACTION")

                        for r in risks:
                            st.write(r)
                    else:
                        st.success(f"CLEAN TRANSACTION [CONFIDENCE: {probas[0]*100:.2f}%]")
                        st.markdown("PASSED CHECKS:")
                        if extract_upi_domain(sender_upi) in ['legitimate_bank', 'legitimate_upi']:
                            st.write("VERIFIED SENDER UPI")
                        if validate_phone(phone):
                            st.write("VALID PHONE FORMAT")
                        if amount <= 50000:
                            st.write("REASONABLE AMOUNT")

# --- Phishing Detection ---
elif page == "🎣 PHISHING DETECTION":
    set_custom_style()
    st.title("🎣 PHISHING DETECTION SYSTEM")
    
    # Header with logo
    st.markdown("""
        <div style="text-align: center; margin-bottom: 2rem;">
            <img src="{logo}" class="logo">
        </div>
    """.format(logo=LOGOS["phishing"]), unsafe_allow_html=True)

    # Load environment variables
    load_dotenv()

    # Configure Gemini
    try:
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    except Exception as e:
        st.error(f"ERROR: Failed to configure Gemini API - {str(e)}")
        st.stop()

    # Specify the new model
    model_name = 'gemini-1.5-flash'
    try:
        model = genai.GenerativeModel(model_name)
        st.info(f"USING MODEL: {model_name}")
    except Exception as e:
        st.error(f"ERROR LOADING MODEL: {e}")
        st.stop()

    # Load Lottie animations with error handling
    def load_lottie_url(url):
        try:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                return r.json()
            return None
        except:
            return None

    safe_animation = load_lottie_url("https://assets1.lottiefiles.com/packages/lf20_jbrw3hcz.json")
    danger_animation = load_lottie_url("https://assets1.lottiefiles.com/packages/lf20_6wutsrox.json")
    scanning_animation = load_lottie_url("https://assets1.lottiefiles.com/packages/lf20_pmvvft6i.json")

    # Website categories database (simplified example)
    WEBSITE_CATEGORIES = {
        "google.com": {"category": "Search Engine", "trust_score": 100},
        "facebook.com": {"category": "Social Media", "trust_score": 90},
        "amazon.com": {"category": "E-Commerce", "trust_score": 95},
        "sgbit.com": {"category": "Unknown", "trust_score": 10},
        "example.com": {"category": "Demo", "trust_score": 50}
    }

    def get_website_category(url):
        """Extract domain and match with known categories"""
        if not url:
            return {"category": "Unknown", "trust_score": 0}
            
        try:
            domain = url.split('//')[-1].split('/')[0].split('?')[0].lower()
            for site, data in WEBSITE_CATEGORIES.items():
                if site in domain:
                    return data
            return {"category": "Unknown", "trust_score": random.randint(10, 60)}
        except:
            return {"category": "Unknown", "trust_score": 0}

    def analyze_url(url):
        """Analyze URL for phishing and return enhanced output"""
        if not url:
            return {"error": "No URL provided", "category": "Unknown", "trust_score": 0}
            
        category_data = get_website_category(url)
        
        prompt = f"""Analyze this URL for phishing risk: {url}
        Respond with ONLY a valid JSON object containing:
        - is_phishing (boolean)
        - confidence (string: Low/Medium/High)
        - reasons (array of strings)
        - safe_to_visit (boolean)
        - website_type (string: Social Media/Banking/E-commerce/etc.)
        - risk_score (integer 0-100)
        - additional_advice (array of strings)

        Example output:
        {{
            "is_phishing": true,
            "confidence": "High",
            "reasons": [
                "Misspelled domain name (sgbit vs sbi)",
                "No SSL certificate",
                "Suspicious login form"
            ],
            "safe_to_visit": false,
            "website_type": "Fake Banking",
            "risk_score": 87,
            "additional_advice": [
                "Do not enter personal information",
                "Check URL carefully",
                "Report to your IT department"
            ]
        }}"""

        try:
            response = model.generate_content(prompt)
            json_str = response.text.strip().replace('```json', '').replace('```', '')
            result = json.loads(json_str)
            result.update(category_data)  # Add category data
            return result
        except Exception as e:
            return {"error": str(e), "category": "Unknown", "trust_score": 0}

    # Streamlit UI for Phishing Detection page
    st.markdown("PROTECT YOURSELF FROM MALICIOUS WEBSITES")
    
    with st.expander("HOW TO USE"):
        st.write("""
        1. Enter any website URL
        2. Click 'Analyze' to check for threats
        3. View security analysis
        4. Get safety recommendations
        """)

    url = st.text_input("ENTER URL TO ANALYZE:", placeholder="https://example.com", key="phish_url")

    if st.button("ANALYZE", key="analyze_btn"):
        if url:
            with st.spinner("SCANNING URL..."):
                # Show scanning animation if available
                if scanning_animation:
                    try:
                        st_lottie(scanning_animation, height=200, key="scanning")
                    except:
                        pass
                
                result = analyze_url(url)
                time.sleep(1)  # Simulate processing time

            st.subheader("ANALYSIS RESULTS")
            
            # Display result
            if "error" in result:
                st.error(f"ERROR: {result['error']}")
            else:
                # Result container with animation
                with st.container():
                    cols = st.columns([1, 3])
                    with cols[0]:
                        if result['is_phishing']:
                            if danger_animation:
                                try:
                                    st_lottie(danger_animation, height=150, key="danger")
                                except:
                                    pass
                            st.error("DANGEROUS WEBSITE")
                        else:
                            if safe_animation:
                                try:
                                    st_lottie(safe_animation, height=150, key="safe")
                                except:
                                    pass
                            st.success("SAFE WEBSITE")
                    
                    with cols[1]:
                        st.metric("RISK SCORE", f"{result.get('risk_score', 0)}/100", 
                                 delta_color="inverse")
                        st.metric("WEBSITE TYPE", result.get('website_type', 'UNKNOWN'))
                        st.metric("CATEGORY", result.get('category', 'UNKNOWN'))
                
                # Detailed results in expandable sections
                with st.expander("DETAILED ANALYSIS", expanded=True):
                    st.write(f"CONFIDENCE LEVEL: {result['confidence']}")
                    
                    # Risk meter
                    risk_score = result.get('risk_score', 0)
                    st.progress(risk_score/100, text=f"RISK METER: {risk_score}%")
                    
                    # Reasons section
                    st.markdown("POTENTIAL RISKS")
                    if result.get("reasons"):
                        for reason in result["reasons"]:
                            st.write(f"> {reason}")
                    else:
                        st.write("No specific risks identified")
                    
                    # Advice section
                    st.markdown("SAFETY RECOMMENDATIONS")
                    if result.get("additional_advice"):
                        for advice in result["additional_advice"]:
                            st.write(f"> {advice}")
                    else:
                        st.write("No specific recommendations")
                
                # Popup notification
                if result['is_phishing']:
                    st.warning("""
                    WARNING: POTENTIAL PHISHING SITE
                    DO NOT ENTER SENSITIVE DATA
                    """, icon="⚠️")
                else:
                    st.balloons()
                    st.success("""
                    CLEAN WEBSITE
                    VERIFY URL BEFORE PROCEEDING
                    """, icon="✅")
                
                # Website comparison (if known)
                if result.get('trust_score', 0) > 0:
                    st.markdown("TRUST COMPARISON")
                    trust_score = result['trust_score']
                    if trust_score > 80:
                        st.success(f"TRUST SCORE: {trust_score}/100 (HIGH)")
                    elif trust_score > 50:
                        st.warning(f"TRUST SCORE: {trust_score}/100 (MEDIUM)")
                    else:
                        st.error(f"TRUST SCORE: {trust_score}/100 (LOW)")
        else:
            st.warning("ERROR: NO URL PROVIDED")

    # Footer with tips
    st.markdown("---")
    st.markdown("""
    SECURITY TIPS:
    - Check for HTTPS
    - Verify domain spelling
    - Beware of unsolicited login pages
    - Hover over links before clicking
    """)