import os
import numpy as np
import tensorflow as tf
import Queue

# Data sets
TRAINING_SET = "windmill_training.csv" # file used for training the tensorflow model
#TEST_SET = "windmill_test.csv"  # file used for testing the accuracy of trained model

sample_value_queue = Queue.Queue()
predictions = []

def main():

  # Load datasets for training
  training_set = tf.contrib.learn.datasets.base.load_csv_with_header(
      filename=TRAINING_SET,
      target_dtype=np.int,
      features_dtype=np.float32)
  '''  
  test_set = tf.contrib.learn.datasets.base.load_csv_with_header(
      filename=TEST_SET,
      target_dtype=np.int,
      features_dtype=np.float32)
  '''
  # Specify that all features have real-value data
  feature_columns = [tf.contrib.layers.real_valued_column("", dimension=1)]


  classifier = tf.contrib.learn.LinearClassifier(feature_columns=feature_columns,
                                              model_dir="/home/shubhamprash/trained_model") # Enter the path where to save the model

  # Define the training inputs
  def get_train_inputs():
    x = tf.constant(training_set.data)
    y = tf.constant(training_set.target)
    return x, y

  # Fit model.
  classifier.fit(input_fn=get_train_inputs, steps=2000)
  '''
  # Define the test inputs
  def get_test_inputs():
    x = tf.constant(test_set.data)
    y = tf.constant(test_set.target)
    return x, y
  '''
  # Evaluate accuracy.
  #  accuracy_score = classifier.evaluate(input_fn=get_test_inputs,
  #                                       steps=1)["accuracy"]

  #  print("\nTest Accuracy: {0:f}\n".format(accuracy_score))

  # New data test

  def new_data():
    if not sample_value_queue.empty():
      value = sample_value_queue.get()
      return np.array([value], dtype=np.float32)

  
  def log_parser():
    with open("./log_container.log","r") as log_file:
      fp = log_file.read()
      log_file_list = fp.split("\n")

      for i in range(0, len(log_file_list)):
        if "Sample Value" in log_file_list[i]:
          temp = log_file_list[i].split(" ")
          sample_value = temp[len(temp) - 1]
          print sample_value
          sample_value_queue.put(sample_value)
          predictions = list(classifier.predict_classes(input_fn=new_data))
  
          print("New data prediction:{}\n".format(predictions))

  log_parser()    


if __name__ == "__main__":
    main()
