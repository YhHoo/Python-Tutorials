#----------------------------------------
# Basics on Building LSTM model on Keras
#----------------------------------------

# as first layer in a sequential model:
model = Sequential()
model.add(Dense(32, input_shape=(16,)))
# now the model will take as input arrays of shape (*, 16)
# and output arrays of shape (*, 32)
# in short, 16 inputs, 32 outputs. * means any num, as in 
# any no of training sets.

# after the first layer, you don't need to specify
# the size of the input anymore:
model.add(Dense(32))


#----------------------------------------
# Validation on Keras model.fit()
#----------------------------------------
model.fit(self.inputs,
		  self.labels,
		  epochs=1000,
		  batch_size=1,
		  verbose=2, # turn this ON to show all acc: and loss:
		  shuffle=False,
          callbacks=callback_list,
		  validation_split=0.33, # Method 1 **
		  validation_data=(X, y)) # Method 2 **
		  
		  # Method 1: directly split the self.inputs and self.labels into 0.33 and 0.66
		  # where 0.33 will not be used for training but validation. the score will be 
		  # printed at the end of every epoch !
		  # Method 2: Manually prepare another set of validation data and the val loss: and acc: 
		  # score will be printed based on these data you put. But be sure to change the validation_split
		  # to 0 !
			