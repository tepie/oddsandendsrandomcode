//
//  zoneclockAppDelegate.h
//  zoneclock
//
//  Created by terrence pietrondi on 11/17/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <UIKit/UIKit.h>

@class zoneclockViewController;

@interface zoneclockAppDelegate : NSObject <UIApplicationDelegate> {
    UIWindow *window;
    zoneclockViewController *viewController;
}

@property (nonatomic, retain) IBOutlet UIWindow *window;
@property (nonatomic, retain) IBOutlet zoneclockViewController *viewController;

@end

