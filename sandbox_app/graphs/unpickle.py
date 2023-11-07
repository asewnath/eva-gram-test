import pickle
import os

files = ['plot_1.pkl', 'plot_2.pkl', 'plot_3.pkl']

for pkl_file in files:
	with open(pkl_file, 'rb') as f:
		loaded_dict = pickle.load(f)

	script = loaded_dict['script']
	div = loaded_dict['div']

	#Write to file
	file_name = os.path.splitext(pkl_file)[0]
	with open(file_name+'_div', 'w') as text_file:
		text_file.write(div)
	with open(file_name+'_script', 'w') as text_file:
		text_file.write(script)
