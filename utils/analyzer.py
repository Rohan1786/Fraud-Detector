# import os
# import magic
# import hashlib
# import random
# import math

# def calculate_entropy(file_path):
#     with open(file_path, 'rb') as f:
#         data = f.read()
#         if not data:
#             return 0
#         byte_counts = [0]*256
#         for byte in data:
#             byte_counts[byte] += 1
#         entropy = 0
#         for count in byte_counts:
#             if count:
#                 p = count / len(data)
#                 entropy -= p * math.log2(p)
#         return entropy

# def get_file_hash(filepath):
#     with open(filepath, "rb") as f:
#         return hashlib.sha256(f.read()).hexdigest()

# def analyze_file(filepath, filename):
#     mime_type = magic.from_file(filepath, mime=True)
#     file_size = os.path.getsize(filepath)
#     entropy = calculate_entropy(filepath)
#     file_hash = get_file_hash(filepath)

#     known_hashes = ["abc123...", "fakebadfilehash123456"]
#     if file_hash in known_hashes:
#         return {
#             'status': 'malicious',
#             'threat_score': 1.0,
#             'method': 'signature',
#             'details': f'{filename} matched known ransomware signature.'
#         }

#     score = round(random.uniform(0, 1), 2)
#     status = 'malicious' if score > 0.7 else 'safe'

#     return {
#         'status': status,
#         'threat_score': score,
#         'method': 'ml',
#         'features': {
#             'mime_type': mime_type,
#             'file_size': file_size,
#             'entropy': round(entropy, 4),
#             'hash': file_hash
#         }
#     }


import os
import magic
import hashlib
import math
import re
from datetime import datetime

# Known malicious indicators
KNOWN_MALICIOUS_HASHES = [
    "a1b2c3d4e5f6...",  # Example ransomware hash
    "7g8h9i0j1k2l3...",  # Example malicious PDF hash
    "4m5n6o7p8q9r0..."   # Example malicious DOCX hash
]

SUSPICIOUS_PATTERNS = [
    r"javascript:", r"eval\(", r"unescape\(", r"shellcode",
    r"powershell", r"cmd\.exe", r"wscript\.shell", r"macro",
    r"\\x[0-9a-f]{2}",  # Hex encoded characters
    r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"  # URLs
]

def calculate_entropy(file_path):
    """Calculate the entropy of a file to detect potential encryption/obfuscation"""
    with open(file_path, 'rb') as f:
        data = f.read()
        if not data:
            return 0
        byte_counts = [0]*256
        for byte in data:
            byte_counts[byte] += 1
        entropy = 0
        for count in byte_counts:
            if count:
                p = count / len(data)
                entropy -= p * math.log2(p)
        return entropy

def get_file_hash(filepath):
    """Calculate SHA256 hash of a file"""
    with open(filepath, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def scan_for_suspicious_content(filepath):
    """Scan file for suspicious patterns"""
    try:
        with open(filepath, 'rb') as f:
            content = f.read().decode('utf-8', errors='ignore')
            
            findings = []
            for pattern in SUSPICIOUS_PATTERNS:
                matches = re.findall(pattern, content, re.IGNORECASE)
                if matches:
                    findings.append({
                        'pattern': pattern,
                        'count': len(matches),
                        'sample': matches[0] if matches else None
                    })
            
            return findings
    except Exception as e:
        return [{'error': str(e)}]

def analyze_file(filepath, filename):
    """Comprehensive file analysis with multiple detection methods"""
    try:
        # Basic file info
        mime_type = magic.from_file(filepath, mime=True)
        file_size = os.path.getsize(filepath)
        file_hash = get_file_hash(filepath)
        
        # Check against known malicious hashes
        if file_hash in KNOWN_MALICIOUS_HASHES:
            return {
                'filename': filename,
                'status': 'malicious',
                'threat_score': 1.0,
                'method': 'signature',
                'details': 'Matched known malicious file signature',
                'mime_type': mime_type,
                'file_size': file_size,
                'entropy': 0,
                'hash': file_hash,
                'suspicious_patterns': []
            }
        
        # Calculate entropy
        entropy = calculate_entropy(filepath)
        
        # Scan for suspicious content
        suspicious_findings = scan_for_suspicious_content(filepath)
        
        # Calculate threat score
        base_score = 0
        
        # Adjust score based on entropy
        entropy_factor = min(max((entropy - 4) / 4, 0), 1)  # Normalize 4-8 to 0-1
        base_score += entropy_factor * 0.4
        
        # Adjust score for suspicious patterns
        if suspicious_findings and not isinstance(suspicious_findings[0], dict):
            # Error case
            pass
        elif suspicious_findings:
            pattern_score = min(len(suspicious_findings) * 0.2, 0.6)
            base_score += pattern_score
        
        # Adjust score for file type
        if mime_type in ['application/x-msdownload', 'application/x-msdos-program']:
            base_score += 0.2
        elif mime_type in ['application/pdf', 'application/msword', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document']:
            base_score += 0.1
        
        # Cap the score at 1.0
        threat_score = min(round(base_score, 2), 1.0)
        
        # Determine status
        if threat_score > 0.85:
            status = 'malicious'
            details = "High threat score based on multiple factors"
        elif threat_score > 0.6:
            status = 'suspicious'
            details = "Suspicious characteristics detected"
        else:
            status = 'safe'
            details = "No significant threats detected"
        
        # Prepare results
        result = {
            'filename': filename,
            'status': status,
            'threat_score': threat_score,
            'method': 'heuristic',
            'details': details,
            'mime_type': mime_type,
            'file_size': file_size,
            'entropy': round(entropy, 4),
            'hash': file_hash,
            'suspicious_patterns': suspicious_findings if suspicious_findings and isinstance(suspicious_findings[0], dict) else []
        }
        
        return result
    
    except Exception as e:
        return {
            'filename': filename,
            'status': 'error',
            'threat_score': 0,
            'method': 'error',
            'details': str(e),
            'mime_type': '',
            'file_size': 0,
            'entropy': 0,
            'hash': '',
            'suspicious_patterns': []
        }