# script to run to check remove header working as expected
import seaborn as sns
import sleepPy.plots as plot
import sleepPy.preprocessing as prep
import pathlib
import sys
sys.path.insert(0, "/Users/angusfisk/Documents/01_PhD_files/"
                   "07_python_package/sleepPy")
sns.set()

# define import dir
input_dir = pathlib.Path(
    "/Users/angusfisk/Documents/01_PhD_files/01_projects"
    "/P3_LLEEG_Chapter3/01_data_files/07_clean_fft_files/")
save_dir = input_dir.parents[1]
subdir_name = "03_analysis_outputs/02_cumulative_plots/02_cumulative_delta"

der_names = ["fro", "occ", "foc"]
subdir_list = []
for der in der_names:
    temp_name = subdir_name + "/" + der
    subdir_list.append(temp_name)

init_kwargs = {
    "input_directory": input_dir,
    "save_directory": save_dir,
    "subdir_name": subdir_name,
    "func": (prep, "read_file_to_df"),
    "search_suffix": ".csv",
    "readfile": True,
    "index_col": [0, 1, 2],
    "header": [0]
}
delta_create_object = prep.SaveObjectPipeline(**init_kwargs)

delta_process_kwargs = {
    "function": (prep, "create_df_for_single_band"),
    "savecsv": False,
    "name_of_band": ["Delta"],
    "range_to_sum": ("0.50Hz", "4.00Hz")
}
delta_create_object.process_file(**delta_process_kwargs)


for der_no, subdir in enumerate(subdir_list):
    init_kwargs["subdir_name"] = subdir
    cumsum_plot_object = prep.SaveObjectPipeline(**init_kwargs)
    process_kwargs = {
        "function": (prep, "create_stage_df"),
        "savecsv": False,
        "object_list": delta_create_object.processed_list,
        "stage_col": "Delta",
        "stages": ["NR", "R"],
        "remove_artefacts": True,
        "other": 0,
        "der_no": der_no,
    }
    cumsum_plot_object.process_file(**process_kwargs)

    plot_kwargs = {
        "function": (plot, "plot_cumulative_from_stage_df"),
        "data_list": cumsum_plot_object.processed_list,
        "remove_col": False,
        "base_freq": "4S",
        "target_freq": "1H",
        "showfig": False,
        "savefig": True,
        "legend_loc": "center right",
        "figsize": (10, 10),
        "scored": False,
        "ylabel": "Cumulative Delta Power during sleep",
        "remove_stages": True,
        "set_file_title": False,
        "set_name_title": True
    }
    cumsum_plot_object.create_plot(**plot_kwargs)
