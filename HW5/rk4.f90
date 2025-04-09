program RungeKutta4
    implicit none
    real(8) :: t, x, dt, k1, k2, k3, k4, t_end
    integer :: n, i

    ! ===========================
    ! First integration: 0 to 10
    ! ===========================
    t = 0.0d0
    x = 1.0d0
    t_end = 10.0d0
    n = 1000
    dt = (t_end - t) / n 
    
    open(unit=10, file="prob3-1.dat", status="replace")
    write(10,*) "t x"
    write(10,*) t, x
    
    do i = 1, n
        k1 = dt * (-x**3 + sin(t))
        k2 = dt * (-(x + 0.5d0*k1)**3 + sin(t + 0.5d0*dt))
        k3 = dt * (-(x + 0.5d0*k2)**3 + sin(t + 0.5d0*dt))
        k4 = dt * (-(x + k3)**3 + sin(t + dt))
        
        x = x + (k1 + 2*k2 + 2*k3 + k4) / 6
        t = t + dt
        
        write(10,*) t, x
    end do
    
    close(10)

    ! ============================
    ! Second integration: 0 to 10000
    ! ============================
    t = 0.0d0
    x = 1.0d0
    t_end = 10000.0d0
    n = 1000
    dt = (t_end - t) / n
    
    open(unit=11, file="prob3-2.dat", status="replace")
    write(11,*) "t x"
    write(11,*) t, x
    
    do i = 1, n
        k1 = dt * (-x**3 + sin(t))
        k2 = dt * (-(x + 0.5d0*k1)**3 + sin(t + 0.5d0*dt))
        k3 = dt * (-(x + 0.5d0*k2)**3 + sin(t + 0.5d0*dt))
        k4 = dt * (-(x + k3)**3 + sin(t + dt))
        
        x = x + (k1 + 2*k2 + 2*k3 + k4) / 6
        t = t + dt
        
        write(11,*) t, x
    end do
    
    close(11)
    print *, "Integration complete. Results saved to prob3-1.dat and prob3-2.dat"
    
end program RungeKutta4
