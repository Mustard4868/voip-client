import numpy as np
import scipy.io.wavfile as wav

def apply_notch_filter(input_wav_file, output_wav_file, notch_freq, Q, volume_scaling):
    sample_rate, data = wav.read(input_wav_file)

    data = data / np.max(np.abs(data), axis=0)

    w0 = 2 * np.pi * notch_freq / sample_rate
    alpha = np.sin(w0) / (2 * Q)
    b = np.array([1, -2 * np.cos(w0), 1])
    a = np.array([1, -2 * alpha * np.cos(w0), alpha**2])

    filtered_data = np.zeros_like(data)

    for i in range(len(data)):
        filtered_data[i] = b[0] * data[i] + b[1] * data[i-1] + b[2] * data[i-2] - a[1] * filtered_data[i-1] - a[2] * filtered_data[i-2]

    filtered_data *= volume_scaling

    wav.write(output_wav_file, sample_rate, np.int16(filtered_data * 32767))

input_wav_file = r"C:\Users\nakad\Downloads\White_Ocean_V.O.F._2_1.wav"
output_wav_file = r'C:\Users\nakad\Downloads\Filt.wav'

notch_frequency = 200.0 
Q_value = 75.0  
volume_scaling_factor = 3.0  
apply_notch_filter(input_wav_file, output_wav_file, notch_frequency, Q_value, volume_scaling_factor)


def generate_advice(notch_freq, Q):
    if notch_freq < 200 or Q < 50:
        advice = "Your current filter settings may not effectively remove the target frequency. Consider increasing the notch frequency or quality factor."
    elif notch_freq > 1000 and Q > 100:
        advice = "Your filter settings are well-tuned to remove the target frequency while preserving audio quality. Good job!"
    else:
        advice = "Your filter settings may need fine-tuning to achieve optimal results. Experiment with different notch frequencies and quality factors."

    return advice

advice = generate_advice(notch_frequency, Q_value)
print("Advice:", advice)

from openpyxl import Workbook

def save_advice_to_excel(filename, data):
    workbook = Workbook()
    
    worksheet = workbook.active
    worksheet.title = "Filter Advice"
    
    worksheet.append(["Notch Frequency", "Q Value", "Advice"])
    
    for advice in data:
        worksheet.append([advice["notch_frequency"], advice["Q_value"], advice["advice"]])
    
    workbook.save(filename)
    print(f"Data saved to {filename}")

advices = [
    {"notch_frequency": 200.0, "Q_value": 75.0, "advice": "Your filter settings may need fine-tuning to achieve optimal results."},
    {"notch_frequency": 300.0, "Q_value": 80.0, "advice": "Your filter settings are well-tuned to remove the target frequency while preserving audio quality. Good job!"}
]

filename = r"C:\Users\nakad\Downloads\NIELS' WORK\database.xlsx"

save_advice_to_excel(filename, advices)
