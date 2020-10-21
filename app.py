#!/usr/bin/python3

import phonenumbers
import streamlit as st
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
from phonenumbers import phonemetadata


def main():
	st.title("Phone Number Location Tracker & Service operator")
	st.subheader("Built With Python")
	mobile = st.text_input("Enter Phone Number")
	if st.button("Track"):
		ch_number = phonenumbers.parse(mobile, 'CH')
		st.success("Country Name {}".format(geocoder.description_for_number(ch_number, "en")))
		service_operator = phonenumbers.parse(mobile, 'RO')
		st.success("Service Operator: {}".format(carrier.name_for_number(service_operator, "en")))
		time_place = phonenumbers.parse(mobile, "RO")
		st.success("The timezone: {}".format(timezone.time_zones_for_geographical_number(time_place)))
		area = phonenumbers.parse(mobile, "CH")
		st.success("Area length: {}".format(geocoder.country_name_for_number(area, "en")))
		meta = phonenumbers.parse(mobile, "EN")
		st.success("Meta Info: {}".format(phonemetadata.PhoneMetadata(meta, "en")))


if __name__ == "__main__":
	main()
