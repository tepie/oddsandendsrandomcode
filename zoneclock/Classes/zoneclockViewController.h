//
//  zoneclockViewController.h
//  zoneclock
//
//  Created by terrence pietrondi on 11/17/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface zoneclockViewController : UIViewController {

	UITextField *estTextField;
	UILabel *cstLabel;
	UILabel *pstLabel;
}

@property (nonatomic,retain) IBOutlet UITextField *estTextField;
@property (nonatomic,retain) IBOutlet UILabel *cstLabel;
@property (nonatomic,retain) IBOutlet UILabel *pstLabel;
- (IBAction) showTime;

@end

