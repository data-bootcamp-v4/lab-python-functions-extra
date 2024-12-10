{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "23e964be-95b4-4edc-b116-94b9fb6d8cb0",
   "metadata": {},
   "outputs": [],
   "source": [
    "def addition_f (num1, num2):\n",
    "    return num1+num2\n",
    "\n",
    "def subtraction_f (num1, num2):\n",
    "    return num1-num2\n",
    "    \n",
    "def multiplication_f (num1,num2):\n",
    "    return num1*num2\n",
    "\n",
    "def division_f (num1,num2):\n",
    "    if num2==0:\n",
    "        return \"Error division 0 not allowed\"\n",
    "    else:\n",
    "         return num1/num2\n",
    "\n",
    "def calculate_f (x,y,z):\n",
    "    if z==\"+\":\n",
    "        return addition (x,y)\n",
    "    elif z==\"-\":\n",
    "        return subtraction (x,y)\n",
    "    elif z==\"*\":\n",
    "        return multiplication (x,y)\n",
    "    elif z==\"/\":\n",
    "        return division (x,y)\n",
    "    else:\n",
    "        return \"Not an valid operator, use: + or - or * or /.\"\n",
    "\n",
    "def get_unique_list_f(lst):\n",
    "    return list(set(lst))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
