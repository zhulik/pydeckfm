default:
	g++ -std=c++23 -o SteamworksPy.so -shared -fPIC SteamworksPy.cpp -l steam_api -L.
