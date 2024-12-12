import sys
sys.path.append("..")
import modules.utils.paths as path


def sampler(df, file_name, size):
  valid_extentions = ["csv", "xls", "xlsx", "json"]
  file_ext = file_name.split(".")[-1] 
  ext = file_ext if file_ext in valid_extentions else "csv"
  
  sample_file_path = path.data_raw_dir(f"sample_{file_name}.{ext}")
  
  df.sample(size).to_csv(sample_file_path, index=False)

  print(f"Muestra guardada en: {sample_file_path}")


if __name__ == "__main__":
  pass