function so =  sim_the_model()

 si = Simulink.SimulationInput('radiator_fan');
 si = si.setModelParameter('StopTime', '10.0');
 so = sim(si);
end