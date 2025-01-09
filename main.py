import argparse
import configparser
import os
import os.path

def get_argparser():
  """Return argument parser.
  Returns:
    Argument parser.
  """
  parser = argparse.ArgumentParser()

  # Specific file paths
  parser.add_argument("--config_path", type=str, default="./config.ini",
                      help="config path (default: ./config.ini)")
  return parser

def parse_config(path: str):
  """Return experiment configuration.
  Args:
    path (str): Path to configuration file (.ini).

  Returns:
    Experiment configuration.
  """
  config = configparser.ConfigParser()
  if not(os.path.exists(path) and os.path.isfile(path) and path.endswith(".ini")):
    raise RuntimeError("Configuration file not found or is not in the right format." +
                       " Double-check that the configuration file is an INI file")
  config.read(path)
  return config

def main():
  opts = get_argparser().parse_args()
  config = parse_config(opts.config_path)
  top_k = config["hyperparameters"]["top_k"]

if __name__ == "__main__":
  main()
