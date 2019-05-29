# Setup guide

1. Install matplotlib: https://matplotlib.org/
2. Donwload datasets: http://bit.ly/2Wwvl2A
3. Place the contents of `h264_results` into the `data_results` directory.
4. Place the contents of `h264_data` into the `data` directory.
5. Change the paths specified in `h264_compare_confidence.py` & `h264_compare_size.py` to the results and dataset which you would like to evaluate.

# How to run

1. Run `h264_compare_confidence.py` & `h264_compare_size.py` in any order.
   - this will create a `h264_results` directory containing `results_confidence.csv` & `results_size.csv` which are to be used in `h264_extract_metrics.py`
2. Run `h264_extract_metrics.py`.
   - this will create `extracted_metric.csv`, `confidence_metrics_for_plotting.csv`, `size_metrics_for_plotting.csv` & `k_metrics_for_plotting.csv`
3. Run `h264_plotter.py`
