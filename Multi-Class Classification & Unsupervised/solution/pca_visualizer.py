def pca_visualizer(X,W,pcs):
    # renderer    
    fig = plt.figure(figsize = (10,5))
    
    # create subplot with 3 panels, plot input function in center plot
    gs = gridspec.GridSpec(1, 2) 
    ax1 = plt.subplot(gs[0],aspect = 'equal');
    ax2 = plt.subplot(gs[1],aspect = 'equal'); 
                 
    # sphere the results
    ars = np.eye(2)
        
    # loop over panels and plot each 
    c = 1
    for ax,pt,ar in zip([ax1,ax2],[X,W],[pcs,ars]): 
        # set viewing limits for originals
        xmin = np.min(pt[0,:])
        xmax = np.max(pt[0,:])
        xgap = (xmax - xmin)*0.15
        xmin -= xgap
        xmax += xgap
        ymin = np.min(pt[1,:])
        ymax = np.max(pt[1,:])
        ygap = (ymax - ymin)*0.15
        ymin -= ygap
        ymax += ygap
    
        # scatter points
        ax.scatter(pt[0,:],pt[1,:],s = 60, c = 'k',edgecolor = 'w',linewidth = 1,zorder = 2)
   
        # plot original vectors
        vector_draw(ar[:,0].flatten(),ax,color = 'red',zorder = 3)
        vector_draw(ar[:,1].flatten(),ax,color = 'red',zorder = 3)

        # plot x and y axes, and clean up
        ax.grid(True, which='both')
        ax.axhline(y=0, color='k', linewidth=1.5,zorder = 1)
        ax.axvline(x=0, color='k', linewidth=1,zorder = 1)
        ax.set_xlim([xmin,xmax])
        ax.set_ylim([ymin,ymax])
        ax.grid('off')

        # set tick label fonts
        for tick in ax.xaxis.get_major_ticks():
            tick.label.set_fontsize(12) 
        for tick in ax.yaxis.get_major_ticks():
            tick.label.set_fontsize(12) 
        
        # plot title
        if c == 1:
            ax.set_title('original space',fontsize = 22)
            ax.set_xlabel(r'$x_1$',fontsize = 22)
            ax.set_ylabel(r'$x_2$',fontsize = 22,rotation = 0,labelpad = 10)
        if c == 2:
            ax.set_title('PCA transformed space',fontsize = 22)
            ax.set_xlabel(r'$v_1$',fontsize = 22)
            ax.set_ylabel(r'$v_2$',fontsize = 22,rotation = 0,labelpad = 10)
        c+=1
