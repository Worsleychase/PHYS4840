program RungeKutta4
    implicit none
    real(8) :: t, x, dt, k1, k2, k3, k4, t_end
    integer :: n, i
    
    ! Define initial conditions
    t = 0.0d0      ! Initial time
    x = 1.0d0      ! Initial condition for x
    dt = 0.1d0     ! Time step
    t_end = 10.0d0 ! Final time
    
    ! Number of time steps
    n = 10000

    ! Open a file to store results
    open(unit=10, file="rk4_results2.dat", status="replace")
    write(10,*) "t x"
    write(10,*) t, x
    
    ! RK4 integration loop
    do i = 1, n
        k1 = dt * (-x**3 + sin(t))
        k2 = dt * (-(x + 0.5d0*k1)**3 + sin(t + 0.5d0*dt))
        k3 = dt * (-(x+0.5d0*k2)**3 + sin(t+0.5d0*dt))
        k4 = dt * (-(x+k3)**3 + sin(t+dt))

        !k3 = h4*f(x+0.5*k2, t+0.5*h4)
        !k4 = h4*f(x+k3, t+h4)
        !x += (k1+2*k2+2*k3+k4)/6
        
        x = x + (k1+2*k2+2*k3+k4)/6
        t = t + dt
        
        ! Write results to file
        write(10,*) t, x
    end do
    
    ! Close file
    close(10)
    
    print *, "Integration complete. Results saved to rk4_results.dat"
    
end program RungeKutta4